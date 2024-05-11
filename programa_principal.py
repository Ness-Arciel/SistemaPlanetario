#!/usr/bin/env python
# coding: utf-8

# ## Programa Principal
# ### El script principal crea un sistema planetario con planetas orbitando un conjunto dado de estrellas e imprime la información pública para los sistemas planetarios, planetas y estrellas. Busca en la base de datos disponible en http://exoplanet.eu todos los planetas que orbitan las estrellas HR 8799, HD 202206, TRAPPIST-1, TOI-1338, HD 188753, Kepler-451 y Kepler-16. La impresión debe indicar si falta algún parámetro en la base de datos.

# In[28]:


import pandas as pd #Importamos Pandas para poder leer los archivos en formato csv.
hr_8799 = pd.read_csv("ROYO4lyz.csv", delimiter=",")
hd_202206 = pd.read_csv("N4UOJRDS.csv", delimiter=",")
Trappist_1 = pd.read_csv("eQ5S4NYi.csv", delimiter=",")
toi_1338 = pd.read_csv("skoUTwB7.csv", delimiter=",")
hd_188753 = pd.read_csv("p5_pPrHA.csv", delimiter=",") #este archivo no contiene datos.
Kepler_451 = pd.read_csv("i8HonHMs.csv", delimiter=",")
Kepler_16 = pd.read_csv("mvsNytjI.csv", delimiter=",")

#vamos a transformarlos a dataframes
hr_8799 = pd.DataFrame(hr_8799)
hd_202206 = pd.DataFrame(hd_202206)
Trappist_1 = pd.DataFrame(Trappist_1)
toi_1338 = pd.DataFrame(toi_1338)
hd_188753 = pd.DataFrame(hd_188753)
Kepler_451 = pd.DataFrame(Kepler_451)
Kepler_16 = pd.DataFrame(Kepler_16)


# In[29]:


# Verificar si hay valores NaN en cada columna
archivos = ["ROYO4lyz.csv", "N4UOJRDS.csv", "eQ5S4NYi.csv", "skoUTwB7.csv", "p5_pPrHA.csv", "i8HonHMs.csv", "mvsNytjI.csv"]
# Lista de nombres de columnas que estás utilizando
columnas_utilizadas = ['star_name', 'star_mass', 'star_radius', 'star_teff', 'star_distance', 'mag_v', 'mass', 'radius', 'semi_major_axis', 'inclination', 'eccentricity', 'omega', 'detection_type']
for archivo in archivos:
    datos = pd.read_csv(archivo, delimiter=",")
    datos = pd.DataFrame(datos)
    
# Verificar si hay valores NaN en las columnas utilizadas
for columna in columnas_utilizadas:
    if columna in datos.columns:
        if datos[columna].isnull().any():
            print(f"El archivo {archivo} tiene valores NaN en la columna '{columna}'")
estrellas = []
sistema_jerarquico = []
planetas = []
exoplanetas = []

for archivo in archivos:
    # Leer el archivo
    datos = pd.read_csv(archivo, delimiter=",")
    # Transformar a DataFrame
    datos = pd.DataFrame(datos)

    # Iterar sobre las filas del DataFrame
    for _, fila in datos.iterrows():
        # Crear objeto Estrella
        estrella = Estrella(fila["star_name"], fila["star_mass"], fila["star_radius"], fila["star_teff"],
                            fila["star_distance"], fila["mag_v"])
        estrellas.append(estrella)

        # Crear objeto SistemaJerarquico
        sistema_jer = SistemaJerarquico([estrella])
        sistema_jerarquico.append(sistema_jer)

        # Crear objeto Planeta
        planeta = Planeta(estrella, fila["mass"], fila["radius"], fila["semi_major_axis"], fila["inclination"],
                          fila["eccentricity"], fila["omega"])
        planetas.append(planeta)

        # Crear objeto Exoplaneta
        exoplaneta = Exoplaneta(estrella, fila["mass"], fila["radius"], fila["semi_major_axis"], fila["inclination"],
                                fila["eccentricity"], fila["mag_v"], fila["detection_type"])
        exoplanetas.append(exoplaneta)
            
class Sistema_Planetario:
    def __init__(self, estrellas, planetas, sistema_jerarquico, exoplanetas):
        self.estrellas = estrellas
        self.planetas = planetas
        self.sistema_jerarquico = sistema_jerarquico
        self.exoplanetas = exoplanetas

    def __str__(self):
        return f"Estrellas: {len(self.estrellas)}, Planetas: {len(self.planetas)}, Sistema Jerarquico: {len(self.sistema_jerarquico)}, Exoplanetas: {len(self.exoplanetas)}"

    def mostrar_detalles(self):
        print("Detalles del Sistema Planetario:")
        for i, estrella in enumerate(self.estrellas):
            print(f"\nEstrella {i+1}: {estrella.nombre}")
            print(f"Luminosidad Total: {estrella.luminosidad_total()}")
            print(f"Luminosidad de la Secuencia: {estrella.luminosidad_secuencia()}")

        print("\nEstrellas ordenadas por masa:")
        sistema_jerarquico = self.sistema_jerarquico[0]  # Asumo que solo hay un sistema jerárquico
        estrellas_ordenadas = sistema_jerarquico.estrellas_masa()
        for estrella in estrellas_ordenadas:
            print(estrella.get_name())

        print("\nNombres de estrellas con letras del alfabeto:")
        nombres_alfabeto = sistema_jerarquico.letra()
        for nombre in nombres_alfabeto:
            print(nombre)

        for planeta in self.planetas:
            print(f"\nPlaneta orbitando a {planeta._anfitriona.nombre}")
            print(f"Periodo de Rotación: {planeta.periodo_rotacion()}")

        for exoplaneta in self.exoplanetas:
            print(f"\nExoplaneta {exoplaneta._anfitriona.nombre}")
            print(f"Método de Descubrimiento: {exoplaneta.metodo_descubrimiento}")
            print(f"¿Similar a Tatooine? {exoplaneta.similar_Tatooine()}")
            #if exoplaneta.metodo_descubrimiento() == "Primary Transit":
            #    print(f"Parámetro de Impacto: {exoplaneta.parametro_impacto()}")


# In[31]:


# Crear 7 sistemas planetarios
sistemas_planetarios = []

for archivo in archivos:
    estrellas = []
    planetas = []
    exoplanetas = []
    
    # Leer el archivo
    datos = pd.read_csv(archivo, delimiter=",")
    datos = pd.DataFrame(datos)

    # Iterar sobre las filas del DataFrame
    for _, fila in datos.iterrows():
        # Crear objeto Estrella
        estrella = Estrella(fila["star_name"], fila["star_mass"], fila["star_radius"], fila["star_teff"],
                            fila["star_distance"], fila["mag_v"])
        estrellas.append(estrella)

        # Crear objeto Planeta
        planeta = Planeta(estrella, fila["mass"], fila["radius"], fila["semi_major_axis"], fila["inclination"],
                          fila["eccentricity"], fila["omega"])
        planetas.append(planeta)

        # Crear objeto Exoplaneta
        exoplaneta = Exoplaneta(estrella, fila["mass"], fila["radius"], fila["semi_major_axis"], fila["inclination"],
                                fila["eccentricity"], fila["mag_v"], fila["detection_type"])
        exoplanetas.append(exoplaneta)
    
    # Crear el sistema planetario correspondiente
    sistema = Sistema_Planetario(estrellas, planetas, sistema_jerarquico, exoplanetas)
    sistemas_planetarios.append(sistema)

# Mostrar los detalles de cada sistema planetario
for i, sistema in enumerate(sistemas_planetarios):
    print(f"\nSistema Planetario {i+1}:")
    sistema.mostrar_detalles()

#La tarea presenta grandes errores y por falta de tiempo me fue imposible terminarla, mil disculpas por todos los errores presentados y muchas gracias por su comprensión :(

