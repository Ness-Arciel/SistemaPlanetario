#!/usr/bin/env python
# coding: utf-8

# ## Planeta
# ### Un planeta es un cuerpo con masa menor que 13 Mjup (masas de Júpiter) que orbita una estrella. Los atributos principales de un planeta son:
# - Su estrella anfritiona (protegido).
# - Masa planetaria (protegido, tipo flotante).
# - Su radio (protegido, tipo flotante).
# - Sus elementos orbitales: radio semi mayor de la órbita _a_, inclinación de la órbita _i_, excentricidad de la órbita _e_, y argumento del periastron _w_ (todos protegidos y tipo flotante).
# ### Para esta clase, se espera que se codifique una función pública que calcule y devuelva el período de rotación kepleriana (retorno de tipo flotante):
# ### T = 2 * pi * raíz(_a_ ³/ G * M)

# In[26]:


#Definimos una nueva clase donde se guarde el elemento Planeta.
class Planeta():
    def __init__(self, anfitriona, masa_planeta, radio_planeta, a, i, e, w):
        self._anfitriona = anfitriona
        self._masa_planeta = masa_planeta
        self._radio_planeta = radio_planeta
        self._a = a
        self._i = i
        self._e = e
        self._w = w
    #Una vez definida nuestra clase Planeta, vamos a crear una función que calcule el periodo de rotación.
    def periodo_rotacion (self):
        G = 6.672e-11 
        M = self._anfitriona._masa #La masa de la estrella anfitriona.
        return 2 * np.pi * np.sqrt((self._a ** 3)/(G * M))
    
    #Creamos una función que calcule la velocidad de escape.
    def velocidad_escape (self):
        G = 6.672e-11
        M = self._masa_planeta
        R = self._radio_planeta
        return np.sqrt((2 * G * M)/R)

