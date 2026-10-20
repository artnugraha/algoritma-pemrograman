import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "../Data/motion.csv",
    delimiter=",",
    names=True
)

t = data["time_s"]
x = data["position_m"]

fig, ax = plt.subplots(figsize=(8.0, 5.4), dpi=180)
ax.plot(t, x, marker="o", linewidth=1.8, markersize=5)

ax.set_xlabel("Waktu, t (s)", fontsize=17)
ax.set_ylabel("Posisi, x (m)", fontsize=17)
ax.set_title("Gerak satu dimensi", fontsize=18)

ax.tick_params(
    axis="both",
    labelsize=14,
    direction="in",
    top=True,
    right=True
)

fig.tight_layout()
fig.savefig(
    "../Gambar/gerak-posisi.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
