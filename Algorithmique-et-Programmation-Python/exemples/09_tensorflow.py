"""Dépendance optionnelle : tensorflow. À installer dans un venv séparé."""

import numpy as np
import tensorflow as tf

tf.keras.utils.set_random_seed(7)
x = np.linspace(0, 1, 40, dtype=np.float32).reshape(-1, 1)
y = 2 * x + 1
model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(1,)),
        tf.keras.layers.Dense(8, activation="tanh"),
        tf.keras.layers.Dense(1),
    ]
)
model.compile(optimizer=tf.keras.optimizers.Adam(0.03), loss="mse")
model.fit(x[:24], y[:24], validation_data=(x[24:30], y[24:30]), epochs=200, verbose=0)
pred = model(x[30:], training=False).numpy()
print("MAE test :", float(np.abs(pred - y[30:]).mean()))
