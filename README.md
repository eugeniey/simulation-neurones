# Dimulations de neurones
Simulation de neurones dans le cerveau selon le modèle de Hodgkin-Huxley


Les neurones sont des cellules nerveuses qui transmettent l'information grâce à des signaux électriques et chimiques. Ils sont formés d'un noyau et de branches appelées dendrites. Ces dernières permettent de transmettre l'information à l'aide de signaux électriques. Elles baignent dans un environnement rempli de différents type d'électrolytes qui sont de bons conducteur. Leurs membranes sont faites d'une substance isolante, ce qui permet de créer une différence de potentiel électrique à l'intérieur des membranes. 

Dans le cadre de ce projet, on simule des neurones et on observe leurs comportements en variant les paramètres les définissant et en variant le courant passant dans les neurones. Les signaux électriques transmettent l'information grâce à un potentiel d'action. Le potentiel d'action est un pic de voltage. Les canaux ioniques dans la membrane (les canaux Na, sodium et K, potassium), gèrent la différence de potentiel transmembranaire. Il est nécessaire de les prendre en compte, car ils influencent le courant et donc le potentiel au repos V.

Le modèle de Hodgkin-Huxley donne la variation temporelle du potentiel membranaire et de la conductance des canaux ioniques. Il est présenté ci-dessous.

![1](https://user-images.githubusercontent.com/47392583/52388684-91536e80-2a5d-11e9-8454-753749bba702.PNG)

Les fonctions-barrières n,m,h permettent de décrire les relations non-linéaires entre les canaux ioniques (K,Na) et le potentiel transmembranaire V. Les termes gK et gNa représentent la conductance des canaux ioniques K et Na. Tandis que le dernier terme de l'équation 1, représente l'effet des canaux ionique autre que le sodium et potassium. Le terme gL représente la conductance de ces autres canaux ioniques de la membrane. 

Le modèle de Hodgkin-Huxley correspond à 4 équations différentielles (EDO) d'ordre 1. Il y a plusieurs méthodes différentes pour solutionner numériquement les équations différentielles d'ordre 1. En général, pour une EDO de type du/dt, on cherche a estimer la valeur de un+1 en utilisant le terme un. Le modèle de Hodgkin-Huxley est résolvable en utilisant la méthode de Runge-Kutta. Celle-ci utilise 4 estimés de pentes pour en faire ensuite la moyenne, décrit ci-dessous

![2](https://user-images.githubusercontent.com/47392583/52388682-91536e80-2a5d-11e9-97dc-cf12072f2a6e.PNG)

La méthode de Runge-Kutta permet d'estimer le terme un+1 avec une moyenne pondérée des quatre estimés de la pente pour estimer le terme un+1. C'est cette estimation que l'on utilise. 

![3](https://user-images.githubusercontent.com/47392583/52388683-91536e80-2a5d-11e9-8c40-a34c4ba3f008.PNG)

On résolve les équations (1) à (4) à l'aide de la méthode de Runga-Kutta, et ainsi, on obtient la variation de ces paramètres dans le temps. 
