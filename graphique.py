from simulation import infoGraph
import numpy as np
import matplotlib.pyplot as plt

# Figure 1
# Variation des paramètres V,m,n,h dans le temps pour un courant de 7
t,u,nn = infoGraph(7)

# Première axe avec le potentiel V 
fig, ax1 = plt.subplots(figsize = (12,8))
ax1.plot(t[:nn], u[:nn, 0], 'k', linewidth=2.5, label='V')
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
ax1.set_xlabel('t [ms]', fontsize = 15)
ax1.set_ylabel('V [mV]', fontsize = 15)

# Deuxième axe avec n,m,h
ax2 = ax1.twinx()
ax2.plot(t[:nn], u[:nn, 1], 'r--', linewidth=2.5, label='n')
ax2.plot(t[:nn], u[:nn, 2], 'b:', linewidth=2.5, label='m')
ax2.plot(t[:nn], u[:nn, 3], 'g-.', linewidth=2.5, label='h')
plt.yticks(fontsize = 12)
ax2.set_ylabel('m, n, h', fontsize = 15)

# Identation secondaire des axes
ax1.set_yticks(np.arange(-20, 121, 5), minor = True)
ax2.set_yticks(np.arange(-0.2, 1.21, 0.05), minor = True)
ax2.set_xticks(np.arange(0, 26, 1), minor = True)
fig.tight_layout()

# Ligne pour les paramètres initiaux 
ax2.axhline(y = u[0,1], color = 'black', linestyle = ':')
ax2.axhline(y = u[0,2], color = 'black', linestyle = ':')
ax2.axhline(y = u[0,3], color = 'black', linestyle = ':')
ax1.axhline(y = u[0,2], color = 'black', linestyle = ':')

ax1.axvspan(0, 1, alpha=0.5, color='grey')

plt.xlim(left=0)
plt.xlim(right=25)
plt.legend(prop={'size': 15})




# Figure 2
# On observe qu'un courant de 6.9 n'est pas assez élevé pour engendré un potentiel d'action

fig, ax = plt.subplots(figsize = (8,6))

x1,y1,nn1 = infoGraph(6.9,eps=1.e-10)
x2,y2,nn2 = infoGraph(7)
x3,y3,nn3 = infoGraph(8)

# Différents courants 
plt.plot(x1[:nn1], y1[:nn1, 0], 'k--', linewidth=2.5, label=r'$I_{a}$ = 6.9 $ \mu A / cm^{2}$')
plt.plot(x2[:nn2], y2[:nn2, 0], 'r:', linewidth=2.5, label=r'$I_{a}$ = 7 $\mu A / cm^{2}$')
plt.plot(x3[:nn3], y3[:nn3, 0], 'b-', linewidth=2.5, label=r'$I_{a}$ = 8 $ \mu A / cm^{2}$')

# Identation secondaire des axes
ax.set_yticks(np.arange(-20, 121, 5), minor = True)
ax.set_xticks(np.arange(0, 26, 1), minor = True)

# Ligne pour les paramètres initiaux
ax.axvspan(0, 1, alpha=0.5, color='grey')

plt.xlim(left=0)
plt.xlim(right=25)
plt.xlabel('t[ms]', fontsize = 12)
plt.ylabel('V[mV]', fontsize = 12)
plt.legend(prop={'size': 15})

plt.show()