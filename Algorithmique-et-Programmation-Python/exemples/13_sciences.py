from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import butter, sosfiltfilt
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).parent / "sorties"
out.mkdir(exist_ok=True)
t = np.linspace(0, 10, 1001)
solution = solve_ivp(
    lambda _, s: [s[1], -0.4 * s[1] - 4 * s[0]],
    (0, 10),
    [0.1, 0],
    t_eval=t,
    rtol=1e-7,
    atol=1e-9,
)
assert solution.success
rc = solve_ivp(
    lambda _, v: [(5 - v[0]) / 0.1],
    (0, 0.5),
    [0],
    t_eval=np.linspace(0, 0.5, 101),
    rtol=1e-8,
    atol=1e-10,
)
assert rc.success
expected = 5 * (1 - np.exp(-1))
assert abs(rc.y[0, 20] - expected) < 1e-6
print(f"RC à tau : {rc.y[0,20]:.6f} V ; référence : {expected:.6f} V")
fs = 100
signal = np.sin(2 * np.pi * t) + 0.3 * np.sin(2 * np.pi * 20 * t)
sos = butter(4, 5, fs=fs, output="sos")
filtered = sosfiltfilt(sos, signal)
fig, axes = plt.subplots(3, 1, figsize=(8, 9))
axes[0].plot(t, solution.y[0])
axes[0].set(title="Oscillateur amorti", xlabel="Temps (s)", ylabel="Position (m)")
axes[1].plot(rc.t, rc.y[0])
axes[1].set(
    title="Circuit RC : R=1 kΩ, C=100 µF", xlabel="Temps (s)", ylabel="Tension (V)"
)
axes[2].plot(t[:200], signal[:200], alpha=0.5, label="Brut")
axes[2].plot(t[:200], filtered[:200], label="Filtré hors ligne")
axes[2].set(
    xlabel="Temps (s)",
    ylabel="Amplitude",
    title="Passe-bas 5 Hz, échantillonnage 100 Hz",
)
axes[2].legend()
fig.tight_layout()
fig.savefig(out / "simulations.png", dpi=160)
plt.close(fig)
print(out / "simulations.png")
