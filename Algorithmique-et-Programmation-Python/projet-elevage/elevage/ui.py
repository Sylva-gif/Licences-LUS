"""Interface Qt ; la logique métier reste dans domain/assistant/storage."""

import csv
import random
import sqlite3
from datetime import date
from PyQt5.QtCore import Qt, QTimer, QElapsedTimer, QDate
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QDoubleSpinBox,
    QComboBox,
    QDateEdit,
    QMessageBox,
    QFileDialog,
    QTextEdit,
    QHeaderView,
    QAbstractItemView,
)
from .storage import utcnow
from .assistant import analyze, answer


class WeightChart(QWidget):
    def __init__(self):
        super().__init__()
        self.values = []
        self.setMinimumHeight(220)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.fillRect(self.rect(), QColor("#ffffff"))
        p.setPen(QColor("#15334a"))
        p.drawText(16, 24, "Historique de poids — kg / date")
        if not self.values:
            p.drawText(16, 65, "Aucune pesée")
            return
        width, height = self.width() - 110, self.height() - 100
        start, end = self.values[0].day, self.values[-1].day
        lo, hi = min(w.kg for w in self.values), max(w.kg for w in self.values)
        spread = max(hi - lo, 1)
        p.drawText(8, 52, f"{hi:.1f}")
        p.drawText(8, 50 + height, f"{lo:.1f}")
        p.drawText(60, self.height() - 20, str(start))
        p.drawText(self.width() - 110, self.height() - 20, str(end))
        p.setPen(QPen(QColor("#00897b"), 3))
        points = [
            (
                60 + width * (w.day - start).days / max((end - start).days, 1),
                50 + height * (hi - w.kg) / spread,
            )
            for w in self.values
        ]
        for a, b in zip(points, points[1:]):
            p.drawLine(int(a[0]), int(a[1]), int(b[0]), int(b[1]))
        p.setBrush(QColor("#00897b"))
        for x, y in points:
            p.drawEllipse(int(x) - 4, int(y) - 4, 8, 8)


class Window(QMainWindow):
    def __init__(self, store):
        super().__init__()
        self.store = store
        self.running = None
        self.clock = QElapsedTimer()
        self.setWindowTitle("Élevage connecté | Licences-LUS")
        self.resize(1180, 820)
        self.setStyleSheet(
            """QMainWindow{background:#eef3f7}
            QLabel{color:#15334a} QPushButton{background:#087f8c;color:white;
            padding:8px;border-radius:4px} QLineEdit,QComboBox,QDoubleSpinBox,QDateEdit{
            padding:5px} QTabWidget::pane{background:white} QTableWidget{background:white}"""
        )
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        self.title = QLabel()
        self.title.setStyleSheet("font-size:23px;font-weight:bold;padding:12px")
        layout.addWidget(self.title)
        layout.addWidget(
            QLabel(
                "Démonstrateur local • données persistantes • décisions validées par l'opérateur"
            )
        )
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        self.animal_select = QComboBox()
        self.build_dashboard()
        self.build_animals()
        self.build_tasks()
        self.build_sensors()
        self.build_assistant()
        self.build_settings()
        self.animal_select.currentIndexChanged.connect(self.refresh_animal)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.refresh()

    def page(self, title):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.tabs.addTab(widget, title)
        return layout

    def button(self, label, callback):
        btn = QPushButton(label)
        btn.clicked.connect(lambda _=False: self.safe(callback))
        return btn

    def safe(self, callback):
        try:
            callback()
        except (ValueError, sqlite3.Error, OSError, csv.Error) as exc:
            QMessageBox.warning(self, "Opération refusée", str(exc))

    def row(self, layout, *widgets):
        row = QHBoxLayout()
        for widget in widgets:
            row.addWidget(widget)
        layout.addLayout(row)

    def table(self, layout, headers):
        table = QTableWidget(0, len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(table)
        return table

    def fill(self, table, rows):
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(value)))

    def spin(self, low, high, initial):
        box = QDoubleSpinBox()
        box.setRange(low, high)
        box.setDecimals(2)
        box.setValue(initial)
        return box

    def build_dashboard(self):
        page = self.page("Tableau de bord")
        self.row(
            page,
            QLabel("Animal"),
            self.animal_select,
            self.button("Actualiser", self.refresh),
        )
        self.kpis = QLabel()
        self.kpis.setStyleSheet("font-size:18px;padding:16px;background:#e1f5ef")
        self.kpis.setWordWrap(True)
        page.addWidget(self.kpis)
        self.chart = WeightChart()
        page.addWidget(self.chart)
        self.alerts = QTextEdit()
        self.alerts.setReadOnly(True)
        page.addWidget(self.alerts)

    def build_animals(self):
        page = self.page("Animaux et pesées")
        self.tag = QLineEdit()
        self.tag.setPlaceholderText("Identifiant unique")
        self.species = QLineEdit("Bovin")
        self.barn = QLineEdit("Atelier A")
        self.row(
            page,
            self.tag,
            self.species,
            self.barn,
            self.button("Ajouter un animal", self.add_animal),
        )
        self.animal_table = self.table(page, ["Identifiant", "Espèce", "Bâtiment"])
        page.addWidget(
            QLabel(
                "Pesée et alimentation : animal sélectionné dans le tableau de bord."
            )
        )
        self.day = QDateEdit(QDate.currentDate())
        self.day.setCalendarPopup(True)
        self.day.setDisplayFormat("yyyy-MM-dd")
        self.day.setMaximumDate(QDate.currentDate())
        self.kg = self.spin(0.01, 5000, 200)
        self.feed = self.spin(0, 500, 4)
        self.row(
            page,
            QLabel("Date"),
            self.day,
            QLabel("Poids kg"),
            self.kg,
            self.button("Enregistrer la pesée", self.add_weight),
        )
        self.row(
            page,
            QLabel("Consommation du jour, kg"),
            self.feed,
            self.button("Enregistrer l'aliment", self.add_feed),
        )
        self.weight_table = self.table(page, ["Date", "Poids kg"])
        self.row(
            page,
            self.button("Exporter toutes les pesées (CSV)", self.export),
            self.button("Charger les données de démonstration", self.demo),
        )

    def animal(self):
        animal_id = self.animal_select.currentData()
        return next((a for a in self.store.animals() if a["id"] == animal_id), None)

    def required_animal(self):
        animal = self.animal()
        if animal is None:
            raise ValueError(
                "Ajouter et sélectionner un animal dans le tableau de bord."
            )
        return animal

    def add_animal(self):
        self.store.add_animal(self.tag.text(), self.species.text(), self.barn.text())
        self.tag.clear()
        self.refresh()

    def add_weight(self):
        self.store.add_weight(
            self.required_animal()["id"],
            self.day.date().toString("yyyy-MM-dd"),
            self.kg.value(),
        )
        self.refresh_animal()

    def add_feed(self):
        self.store.add_feed(
            self.required_animal()["id"],
            self.day.date().toString("yyyy-MM-dd"),
            self.feed.value(),
        )
        self.refresh_animal()
        self.statusBar().showMessage("Consommation journalière enregistrée", 5000)

    def export(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Exporter", "pesees.csv", "CSV (*.csv)"
        )
        if path:
            self.store.export_weights(path)

    def demo(self):
        if not self.store.demo():
            QMessageBox.information(
                self,
                "Démonstration",
                "Disponible uniquement sur une base sans animaux.",
            )
        self.refresh()

    def build_tasks(self):
        page = self.page("Projet et temps")
        self.task_title = QLineEdit()
        self.task_title.setPlaceholderText("Nom de la tâche")
        self.planned = self.spin(1, 100000, 30)
        self.row(
            page,
            self.task_title,
            QLabel("Budget min"),
            self.planned,
            self.button("Créer une tâche", self.add_task),
        )
        self.task_select = QComboBox()
        self.row(
            page,
            self.task_select,
            self.button("Démarrer", self.start_task),
            self.button("Arrêter / enregistrer", self.stop_task),
            self.button("Marquer terminée", self.finish_task),
        )
        self.elapsed = QLabel("Aucun chronomètre actif")
        page.addWidget(self.elapsed)
        self.task_table = self.table(
            page, ["ID", "Tâche", "Prévu min", "Réel min", "Écart min", "État"]
        )
        page.addWidget(
            QLabel(
                "Un chronomètre à la fois. Le temps actif est sauvegardé à l'arrêt ou à la fermeture normale."
            )
        )

    def add_task(self):
        self.store.add_task(self.task_title.text(), self.planned.value())
        self.task_title.clear()
        self.refresh_tasks()

    def start_task(self):
        if self.running:
            raise ValueError("Arrêter d'abord le chronomètre actif.")
        task_id = self.task_select.currentData()
        if task_id is None:
            raise ValueError("Aucune tâche ouverte.")
        self.running = (task_id, utcnow().isoformat())
        self.clock.start()
        self.tick()

    def stop_task(self):
        if self.running:
            self.store.add_session(
                self.running[0], self.running[1], self.clock.elapsed() / 1000
            )
            self.running = None
            self.refresh_tasks()
            self.tick()

    def finish_task(self):
        task_id = self.task_select.currentData()
        if task_id is None:
            raise ValueError("Aucune tâche ouverte.")
        if self.running and self.running[0] == task_id:
            self.stop_task()
        self.store.finish_task(task_id)
        self.refresh_tasks()

    def tick(self):
        self.elapsed.setText(
            f"Tâche {self.running[0]} : {self.clock.elapsed()/1000:.0f} s"
            if self.running
            else "Aucun chronomètre actif"
        )

    def refresh_tasks(self):
        selected = self.task_select.currentData()
        self.task_select.clear()
        rows = self.store.tasks()
        for t in rows:
            if not t["done"]:
                self.task_select.addItem(t["title"], t["id"])
        index = self.task_select.findData(selected)
        if index >= 0:
            self.task_select.setCurrentIndex(index)
        self.fill(
            self.task_table,
            [
                (
                    t["id"],
                    t["title"],
                    t["planned_minutes"],
                    round(t["seconds"] / 60, 2),
                    round(t["seconds"] / 60 - t["planned_minutes"], 2),
                    "Terminée" if t["done"] else "Ouverte",
                )
                for t in rows
            ],
        )

    def build_sensors(self):
        page = self.page("Capteurs IoT")
        page.addWidget(
            QLabel(
                "Les simulations sont étiquetées. Les imports CSV utilisent des horodatages avec fuseau."
            )
        )
        self.sensor_barn = QLineEdit("Atelier A")
        self.row(
            page,
            QLabel("Bâtiment"),
            self.sensor_barn,
            self.button("Simuler une mesure", self.simulate),
            self.button("Importer CSV", self.import_csv),
        )
        self.sensor_table = self.table(
            page, ["Bâtiment", "Date UTC", "°C", "Humidité %", "Source"]
        )

    def simulate(self):
        self.store.add_sensor(
            self.sensor_barn.text(),
            utcnow().isoformat(),
            round(random.uniform(20, 34), 1),
            round(random.uniform(40, 80), 1),
        )
        self.refresh_sensors()
        self.refresh_animal()

    def import_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Mesures capteurs", "", "CSV (*.csv)"
        )
        if path:
            count = self.store.import_sensors(path)
            self.refresh_sensors()
            self.refresh_animal()
            self.statusBar().showMessage(f"{count} mesures importées", 5000)

    def refresh_sensors(self):
        self.fill(
            self.sensor_table,
            [
                (
                    s["barn"],
                    s["measured_at"],
                    s["temperature"],
                    s["humidity"],
                    s["source"],
                )
                for s in self.store.sensors()
            ],
        )

    def build_assistant(self):
        page = self.page("Assistant IA local")
        page.addWidget(
            QLabel(
                "Animal du tableau de bord • règles explicables + régression OLS • aucun service externe"
            )
        )
        self.question = QLineEdit(
            "Quel est le bilan de croissance et quelles alertes vérifier ?"
        )
        self.row(page, self.question, self.button("Analyser", self.ask))
        self.response = QTextEdit()
        self.response.setReadOnly(True)
        page.addWidget(self.response)

    def ask(self):
        self.response.setPlainText(
            answer(self.store, self.required_animal(), self.question.text())
        )

    def build_settings(self):
        page = self.page("Paramètres")
        settings = self.store.settings()
        self.project = QLineEdit(settings["project"])
        self.gmq_min = self.spin(-10000, 10000, float(settings["gmq_min"]))
        self.temp_max = self.spin(-50, 70, float(settings["temp_max"]))
        self.row(page, QLabel("Projet"), self.project)
        self.row(page, QLabel("Seuil pédagogique GMQ, g/j"), self.gmq_min)
        self.row(page, QLabel("Seuil pédagogique température, °C"), self.temp_max)
        page.addWidget(self.button("Enregistrer les paramètres", self.save_settings))
        note = QLabel(
            "Seuils de démonstration : ils ne constituent pas des références zootechniques.\n"
            "À calibrer pour chaque espèce, âge, lot et contexte avec un professionnel.\n"
            "Une base représente un projet ; utiliser --db pour ouvrir un autre projet.\n"
            "Les doublons sont refusés. La correction de données est un exercice d'extension."
        )
        note.setWordWrap(True)
        page.addWidget(note)
        page.addStretch()

    def save_settings(self):
        self.store.save_settings(
            self.project.text(), self.gmq_min.value(), self.temp_max.value()
        )
        self.refresh()

    def refresh_animal(self, *_):
        animal = self.animal()
        if not animal:
            self.kpis.setText("Ajouter un animal ou charger la démonstration.")
            self.chart.values = []
            self.chart.update()
            self.alerts.clear()
            self.weight_table.setRowCount(0)
            return
        data = analyze(self.store, animal)
        weights = self.store.weights(animal["id"])
        rate = "N/D" if data["gmq"] is None else f"{data['gmq']:.1f} g/j"
        ratio = "N/D" if data["ic"] is None else f"{data['ic']:.2f} kg/kg"
        self.kpis.setText(
            f"{animal['tag']} • GMQ : {rate} • IC : {ratio} • {len(weights)} pesées"
        )
        self.chart.values = weights
        self.chart.update()
        self.alerts.setPlainText("\n\n".join(data["messages"]))
        self.fill(self.weight_table, [(w.day, f"{w.kg:.2f}") for w in weights])
        self.response.clear()

    def refresh(self):
        self.title.setText(self.store.settings()["project"])
        selected = self.animal_select.currentData()
        self.animal_select.blockSignals(True)
        self.animal_select.clear()
        animals = self.store.animals()
        for a in animals:
            self.animal_select.addItem(a["tag"], a["id"])
        index = self.animal_select.findData(selected)
        if index >= 0:
            self.animal_select.setCurrentIndex(index)
        self.animal_select.blockSignals(False)
        self.fill(
            self.animal_table, [(a["tag"], a["species"], a["barn"]) for a in animals]
        )
        self.refresh_animal()
        self.refresh_tasks()
        self.refresh_sensors()

    def closeEvent(self, event):
        try:
            self.stop_task()
        except (ValueError, sqlite3.Error) as exc:
            QMessageBox.warning(self, "Sauvegarde impossible", str(exc))
            event.ignore()
            return
        event.accept()
