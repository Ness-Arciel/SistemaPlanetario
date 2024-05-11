#!/usr/bin/env python
# coding: utf-8

# ## Sistema Jerárquico
# ### Un sistema jerárquico es un sistema estelar múltiple compuesto por N >= 2 estrellas. Los atributos principales del sistema estelar son:
# - La lista de estrellas que contiene (tipo lista).  
# ### Se espera que se codifique las siguientes funciones para esta clase:
# - Una función pública que devuelva la lista de estrellas ordenada por masa estelar (tipo lista).
# - Una función pública que imprima los nombres de las estrellas seguidos por la lista ordenada de letras del alfabeto (Por ejemplo, SirioA, SirioB) (tipo cadena de texto).

# In[1]:


#Creamos una nueva clase, donde se englobe el tema de un sistema jerárquico.
class SistemaJerarquico():
    """
    Se define la clase SistemaJerarquico, la cual contiene las siguientes instancias:
    - estrellas: Grupo de estrellas.

    Se definen tres funciones:
    - sistema_multiple (self): Ordena los nombres estrellas por masa.
    - estrellas_masa (self): Filtra los nombres de las estrellas por su masa.
    - letra (self): Agrega una letra del abecedario a cada nombre de la estrella.
    """
    def __init__ (self, estrellas): #Llamamos estrellas a un grupo de estrellas, distinta a la clase Estrella.
        self.estrellas = estrellas
    #Creamos una función que devuelva el nombre de las estrellas correspondientes al sistema Jerárquico.
    def sistema_multiple(self):
        estrellas_ordenadas = sorted(self.estrellas, key=lambda estrella: estrella._masa)
        return estrellas_ordenadas
        
    #Creamos otra función donde filtramos los nombres de las estrellas por su masa.
    def estrellas_masa(self):
        return sorted(self.estrellas, key=lambda estrella: estrella._masa)
    
    #Creamos otra función donde filtramos el nombre de las estrellas y se le agrega una letra.
    def letra(self):
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nombres = []

        for i, estrella in enumerate(self.estrellas):
            letra = alfabeto[i % len(alfabeto)]  #aqui se toma el modulo de la longitud del alfabeto
            nombre = f"{estrella.nombre}{letra}"
            nombres.append(nombre)

        return nombres

