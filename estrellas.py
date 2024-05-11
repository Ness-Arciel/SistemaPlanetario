#!/usr/bin/env python
# coding: utf-8

# ## Estrellas
# ### Los atributos principales de una estrella son:
# - Su nombre (por ejemplo, Sirio) (público).
# - Masa M (protegido).
# - Radio $R_*$ (protegido).
# - Temperatura superficial _Teff_ (protegido).
# - Distancia d (protegido).
# - Movimiento Propio $\vec{\Delta}$ (vector de dos dimensiones para la velocidad proyectada en el cielo) (protegido).
# 
# Se espera que codifique las siguientes funciones para esta clase:
# - Una función pública (con retorno de tipo flotante) que calcule la luminosidad total $L = 4 \cdot \pi \cdot R^2 \cdot T_eff_.$
# - Una función pública (con retorno de tipo flotante) que calcule la luminosidad de la secuencia principal $Lms = Lsun \cdot (\frac{M}{Msun})^ {3.5}$
# 
# Utilice las siguientes constantes: $Lsun = 3.828 \cdot 10 ^ {26}  W$ y $Msun = 1.9884 \cdot 10 ^ {30}  kg$. También puede buscar las constantes en scipy o astropy si así lo desea.

# In[12]:


#Importamos las librerías necesarias.
import numpy as np

#Definimos nuestra clase Estrella.
class Estrella():
    """
    Se define la clase Estrella, la cual contiene las siguientes instancias:
    - nombre: Nombre de la estrella.
    - _masa: Masa de la estrella (atributo protegido).
    - _radio: Radio de la estrella (atributo protegido).
    - _temperatura: Temperatura superficiel de la estrella (atributo protegido).
    - _distancia: Distancia de la estrella (atributo protegido).
    - _movimiento: Movimiento propio de la estrella (atributo protegido).

    Se definen tres funciones:
    - luminosidad_total (self): Calcula la luminosidad total de la estrella con la fórmula L = 4 * pi * R^2 * T_eff_.
    - luminosidad_secuencia (self): Calcula la luminosidad de la secuencia principal de la estrella con la fórmula 
                                    L_ms = L_sun * (M/M_sun)**3.5
    - get_name (self): Obtiene el nombre de la estrella.
    """
    def __init__(self, nombre, masa, radio, sup_temperatura, distancia, movimiento):
        self.nombre = nombre
        self._masa = masa     #El guion bajo vuelve el atributo protegido.
        self._radio = radio
        self._temperatura = sup_temperatura
        self._distancia = distancia
        self._movimiento = movimiento

#Una vez definida nuestra clase, creamos las siguientes funciones pertenecientes al mismo objeto Estrella.
    def luminosidad_total(self):
        return 4 * np.pi * (self._radio**2) * self._temperatura #Creamos una función pura.
    
    #Ahora creamos la siguiente función que calcula la luminosidad de la secuencia
    def  luminosidad_secuencia (self):
        L_sun = 3.828e26 #W
        M_sun = 1.9884e30 #Kg
        return L_sun * (self._masa / M_sun)**3.5
    def get_name(self): #obtenemos el nombre de la estrella
        return self.nombre

