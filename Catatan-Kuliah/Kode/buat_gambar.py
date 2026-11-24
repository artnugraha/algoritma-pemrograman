from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size':14,'axes.labelsize':18,'xtick.labelsize':14,'ytick.labelsize':14,'legend.fontsize':13,'axes.linewidth':1.1,'svg.fonttype':'none'})
def save(fig,name):
    fig.tight_layout()
    for ext in ('png','svg'):
        fig.savefig(p/'Gambar'/f'{name}.{ext}',dpi=300)
    plt.close(fig)
def axes():
    fig,ax=plt.subplots(figsize=(8,5.4))
    ax.tick_params(which='both',direction='in',top=True,right=True)
    return fig,ax
n=np.geomspace(2,1e6,400)
fig,ax=axes()
for y,label,ls in [(np.ones_like(n),'1',':'),(np.log2(n),r'$\log_2 N$','--'),(n,r'$N$','-.'),(n*n,r'$N^2$','-')]:
    ax.loglog(n,y,label=label,ls=ls,lw=2)
ax.set(xlabel='Jumlah elemen, $N$',ylabel='Pertumbuhan fungsi (tak berdimensi)')
ax.legend(); save(fig,'kompleksitas')
n=np.unique(np.geomspace(1,1e6,600).astype(int))
fig,ax=axes()
ax.loglog(n,n,label='Beruntun',lw=2)
ax.step(n,np.floor(np.log2(n))+1,where='post',label='Biner',lw=2)
ax.set(xlabel='Jumlah elemen, $N$',ylabel='Jumlah pemeriksaan maksimum')
ax.legend(); save(fig,'jumlah-pemeriksaan')
fig,ax=plt.subplots(figsize=(9,3.8))
ax.set_xlim(-1.5,7.1); ax.set_ylim(-.2,3.3); ax.axis('off')
vals=[2,5,8,12,16,23,38]
for y,lo,hi,mid in [(2,0,6,3),(.6,4,6,5)]:
    ax.text(-.2,y+.35,'Langkah '+('1' if y==2 else '2'),ha='right',va='center',fontsize=13)
    for i,v in enumerate(vals):
        active=lo<=i<=hi
        ax.add_patch(Rectangle((i,y),.88,.7,facecolor=('#c8dfed' if i==mid else 'white' if active else '#eeeeee'),edgecolor='#333333' if active else '#bbbbbb',lw=1.4))
        ax.text(i+.44,y+.35,str(v),ha='center',va='center',fontsize=16,color='#222222' if active else '#888888')
        ax.text(i+.44,y-.12,str(i),ha='center',va='top',fontsize=11)
    ax.text(mid+.44,y+.78,'mid'+(' = target' if mid==5 else ''),ha='center',fontsize=12)
save(fig,'pencarian-biner')
w=np.arange(400,701,5)
intensity=np.exp(-.5*((w-550)/35)**2)
np.savetxt(p/'Data/spektrum.csv',np.column_stack([w,intensity]),delimiter=',',header='wavelength_nm,relative_intensity',comments='',fmt=['%d','%.8f'])
