import numpy as np
import matplotlib.pyplot as plt


# Fonctions calculant les paramètres nécessaires
def alpha_n(V): return (0.1-0.01*V) / (np.exp(1-0.1*V)-1)
def beta_n(V): return 0.125 * np.exp(-V/80)

def alpha_m(V): return (2.5-0.1*V) / (np.exp(2.5-0.1*V)-1)
def beta_m(V): return 4 * np.exp(-V/18)

def alpha_h(V): return 0.07 * np.exp(-V/20)
def beta_h(V): return 1 / (np.exp(3-0.1*V)+1)

'''
Fonction qui calcule le côté droit du système EDO
t0: temps (ms)
u: contient les différents paramètres u = (V,n,m,h) 
Ia: courant initial
gx: tableau contenant la conductance des canaux ioniques gx = (gK,gNa,gL)
Vx: tableau contenant les valeurs des potentiels au repos pour K,Na,L
cm: capacité de la membrane
'''
def g(t0,u,Ia,gx,Vx,cm,continu):

	if not(continu):
		if t0>1: Ia=0

	t1 = gx[0] * u[1]**4 * (u[0]-Vx[0])
	t2 = gx[1] * u[2]**3 * u[3] * (u[0]-Vx[1])
	t3 = gx[2] * (u[0]-Vx[2])

	dV_dt = 1/cm * ( Ia - t1  - t2 - t3 )
	dn_dt = alpha_n(u[0]) * (1-u[1]) - beta_n(u[0]) * u[1]
	dm_dt = alpha_m(u[0]) * (1-u[2]) - beta_m(u[0]) * u[2]
	dh_dt = alpha_h(u[0]) * (1-u[3]) - beta_h(u[0]) * u[3]

	eval = np.array([dV_dt,dn_dt,dm_dt,dh_dt]) 
	return eval
	

# Fonction qui calcule un seul pas de Runge-Kutta
def rk(h,t0,uu,Ia,gx,Vx,cm,continu):

	h2 = h / 2.

	g1 = g(t0,      uu,           Ia, gx, Vx, cm,continu) 
	g2 = g(t0 + h2, uu + h2 * g1, Ia, gx, Vx, cm,continu) 
	g3 = g(t0 + h2, uu + h2 * g2, Ia, gx, Vx, cm,continu) 
	g4 = g(t0 + h , uu + h * g3 , Ia, gx, Vx, cm,continu) 
	
	unew = uu + h/6. * (g1 + 2.*g2 + 2.*g3 + g4) 
	return unew

'''
 Fonction qui calcule V,n,m,h 
 Ia_initial: le courant initiale
 continu:    si le courant est continue ou non
 tfin:       temps de fin
 eps:        tolérence pour précision
 nMax:       nombre d'itération maximal
 g_L:        conductance du canal ionique pour L
 Retourne les valeurs de temps, u et nn (itération temporelle)
'''
def infoGraph(Ia_initial, continu=False, tfin=25, eps = 1.e-8, nMax=10000, g_L = 0.3, temps_courant=1):

		t = np.zeros(nMax)      # tableau temps
		u = np.zeros([nMax,4])  # tableau solution
		nn = 0                  # compteur iterations temporelles
		h = 0.1                 # le pas initial
		cm = 1                  # capacité

		# Valeur des paramètres initiaux que l'on veut calculé
		V = 0
		n_ini = alpha_n(V)/(alpha_n(V)+beta_n(V))
		m_ini = alpha_m(V)/(alpha_m(V)+beta_m(V))
		h_ini = alpha_h(V)/(alpha_h(V)+beta_h(V))
		u[0,:] = np.array([V, n_ini, m_ini, h_ini])
		
		# Coefficient de conductance
		g_K = 36
		g_Na = 120
		gx = np.array([g_K,g_Na,g_L])
		
		# Potentiel de repos
		V_K = -12
		V_Na = 115
		V_L = 10.6 
		Vx = np.array([V_K,V_Na,V_L])

		# Valeur de courant initial
		Ia = Ia_initial

		while (t[nn] < tfin) and (nn < (nMax-1)): 
	
			h2 = h/2.

			u1  = rk(h,  t[nn], u[nn,:], Ia, gx, Vx, cm,continu) 
			u2a = rk(h2, t[nn], u[nn,:], Ia, gx, Vx, cm,continu)
			u2  = rk(h2, t[nn], u2a[:],  Ia, gx, Vx, cm,continu) 
			
			delta = max(abs(u2[0]-u1[0]), abs(u2[1]-u1[1]), abs(u2[2]-u1[2]), abs(u2[3]-u1[3]))
			
			if delta > eps: h/=1.5 

			# On accepte le pas
			else:               
				nn = nn + 1
				t[nn] = t[nn-1] + h         # le nouveau pas de temps
				u[nn,:] = u2[:]             # la solution a ce pas
				if delta <= eps/2.: h*=1.5  # on augmente le pas

		return t, u, nn