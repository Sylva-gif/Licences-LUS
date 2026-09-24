import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

x = np.arange(40, dtype=float).reshape(-1, 1)
y = 180 + 0.8 * x[:, 0] + np.sin(x[:, 0])
model = make_pipeline(StandardScaler(), Ridge(alpha=0.1))
model.fit(x[:30], y[:30])
mae = mean_absolute_error(y[30:], model.predict(x[30:]))
baseline = mean_absolute_error(y[30:], np.full(10, y[29]))
print(f"MAE modèle : {mae:.3f} kg ; baseline : {baseline:.3f} kg")
assert mae < baseline
