#!/usr/bin/env python
# coding: utf-8

# ## Planeta Exoplanetario
# ### Un exoplaneta es un planeta con una estrella anfitriona que no es el Sol. Un exoplaneta hereda de planeta. Sin embargo, tiene dos funciones públicas adicionales. La primera determina el método de primer descubrimiento, si por "imagen directa", "velocidad radial, o "tránsito". La segunda determina si el planeta es similar a Tatooine  (por ejemplo, un planeta orbitando una estrella binaria). Si el planeta es un tránsito, informa adicionalmente su "parámetro de impacto" b:
# $b = a \cdot  cos(i) \frac{1 - e^2}{[R_*(1 + e \cdot sin (w))]}$
# 
# ### Para un exoplaneta en tránsito, 0 < b < 1.

# In[27]:


#Como el planeta exoplanetario es heredado de planeta, creamos una clase heredada.
class Exoplaneta(Planeta):
    """
    Se define la clase Exoplaneta que hereda de la clase Planeta, la cual contiene las siguientes instancias:
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
    def __init__ (self, anfitriona, masa_planeta, radio_planeta, a, i, e, w, metodo_descubrimiento):
        Planeta.__init__(self, anfitriona, masa_planeta, radio_planeta, a, i, e, w)
        self.metodo_descubrimiento = metodo_descubrimiento #Definimos el metodo de descubrimiento.
    def metodo_descubrimiento (self):
        return self.metodo_descubrimiento
    
    def similar_Tatooine (self): #Que sea similar a tatooine significa que el planeta está en un sistema binaro.
        if type(self._anfitriona) == SistemaJerarquico: #Aqui decimos que si la estrella anfitriona forma parte de un sistema jerárquico (sistema con dos o más estrellas)
            similar_Tatooine = True                     #Entonces significa que el planeta es similar a Tatooine.
        else:
            similar_Tatooine = False
    def parametro_impacto (self):
        if self.metodo_descubrimiento == "Primary Transit":
            r_estrella = self._anfitriona._ratio
            return (self._a * np.cos(self._i)) * ((1 - (self._e)**2)/((r_estrella) * (1 + self._e * np.sin(self._w))))

