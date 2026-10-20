import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    "../Data/cooling.csv",
    delimiter=",",
    names=True
)

t = data["time_min"]
T = data["temperature_C"]

print(f"Jumlah data      : {T.size}")
print(f"Temperatur awal  : {T[0]:.3f} C")
print(f"Temperatur akhir : {T[-1]:.3f} C")
print(f"Temperatur min   : {T.min():.3f} C")
print(f"Temperatur max   : {T.max():.3f} C")
print(f"Temperatur rata2 : {T.mean():.3f} C")

fig, ax = plt.subplots(figsize=(8.0, 5.4), dpi=180)
ax.plot(t, T, marker="o", linewidth=1.8, markersize=5)

ax.set_xlabel("Waktu, t (menit)", fontsize=17)
ax.set_ylabel("Temperatur, T (°C)", fontsize=17)
ax.set_title("Pendinginan benda", fontsize=18)

ax.tick_params(
    axis="both",
    labelsize=14,
    direction="in",
    top=True,
    right=True
)

fig.tight_layout()
fig.savefig(
    "../Gambar/pendinginan.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
