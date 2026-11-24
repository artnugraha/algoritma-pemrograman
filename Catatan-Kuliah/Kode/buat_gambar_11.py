from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MaxNLocator

root = Path(__file__).resolve().parent.parent
out = root / 'Gambar'
out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 14, 'axes.labelsize': 18, 'xtick.labelsize': 15, 'ytick.labelsize': 15, 'legend.fontsize': 14, 'axes.linewidth': 1.1, 'svg.fonttype': 'none'})

def save(fig, ax, name, minor=True):
    ax.tick_params(which='major', direction='in', top=True, right=True, length=6, width=1.1)
    ax.tick_params(which='minor', direction='in', top=True, right=True, length=3)
    if minor:
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    fig.tight_layout()
    for ext in ('png', 'svg'):
        fig.savefig(out / f'{name}.{ext}', dpi=300, bbox_inches='tight')
    plt.close(fig)

n = np.logspace(1, 5, 300)
fig, ax = plt.subplots(figsize=(7.6, 5.0))
ax.loglog(n, n, lw=2, label=r'$N$')
ax.loglog(n, n*np.log2(n), lw=2, ls='--', label=r'$N\log_2 N$')
ax.loglog(n, n*n, lw=2, ls='-.', label=r'$N^2$')
ax.set_xlabel(r'Jumlah data, $N$')
ax.set_ylabel('Skala pertumbuhan (tak berdimensi)')
ax.legend(frameon=False, loc='upper left')
save(fig, ax, 'kompleksitas', minor=False)

e = np.loadtxt(root/'Data'/'energi.csv', delimiter=',', skiprows=1)[:,1]
i = np.arange(1, e.size+1)
fig, ax = plt.subplots(figsize=(7.6, 5.0))
ax.plot(i, e, 'o--', lw=1.6, ms=7, label='Urutan awal')
ax.plot(i, np.sort(e), 's-', lw=2, ms=7, label='Urutan menaik')
ax.axhline(np.median(e), color='0.4', ls=':', lw=1.4, label='Median')
ax.set_xlabel('Nomor elemen dalam urutan')
ax.set_ylabel(r'Energi kinetik, $E$ (J)')
ax.set_xticks(i)
ax.set_ylim(0, 11)
ax.legend(frameon=False, loc='upper left')
save(fig, ax, 'energi')
