"""Lancement : python main.py --demo ; --smoke pour vérifier Qt sans interaction."""

import argparse
import sys
from pathlib import Path
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from elevage.storage import Store
from elevage.ui import Window


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db", default=str(Path.home() / "ElevageConnecte" / "elevage.sqlite3")
    )
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument(
        "--screenshot", help="Exporter une capture PNG lors du test --smoke"
    )
    args = parser.parse_args()
    app = QApplication(sys.argv[:1])
    store = Store(args.db)
    try:
        if args.demo:
            store.demo()
        window = Window(store)
        window.show()
        if args.smoke:

            def finish():
                if args.screenshot:
                    window.grab().save(args.screenshot)
                window.close()
                app.quit()

            QTimer.singleShot(500, finish)
        return app.exec_()
    finally:
        store.close()


if __name__ == "__main__":
    raise SystemExit(main())
