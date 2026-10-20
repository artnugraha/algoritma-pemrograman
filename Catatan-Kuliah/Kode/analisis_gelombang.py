import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "../Data/wave.csv",
    delimiter=",",
    names=True
)

t = data["time_s"]
y = data["displacement_m"]

amplitude = np.max(np.abs(y))
rms = np.sqrt(np.mean(y**2))

print(f"Amplitudo numerik : {amplitude:.6f} m")
print(f"RMS numerik       : {rms:.6f} m")
print(f"A/sqrt(2)         : {amplitude / np.sqrt(2):.6f} m")

fig, ax = plt.subplots(figsize=(8.0, 5.4), dpi=180)
ax.plot(t, y, linewidth=1.8)

ax.set_xlabel("Waktu, t (s)", fontsize=17)
ax.set_ylabel("Simpangan, y (m)", fontsize=17)
ax.set_title("Gelombang sinus sintetis", fontsize=18)

ax.tick_params(
    axis="both",
    labelsize=14,
    direction="in",
    top=True,
    right=True
)

fig.tight_layout()
fig.savefig(
    "../Gambar/gelombang.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
