# Sistema Planetario

Este repositorio contiene clases Python para generar un sistema estelar a partir de archivos con estrellas, sistemas jerárquicos de estrellas, planetas y exoplanetas. Además, incluye funciones para realizar cálculos y operaciones relacionadas con la astronomía y la astrofísica.

## Clase Estrella

La clase Estrella modela una estrella y proporciona métodos para calcular propiedades como luminosidad total, luminosidad de la secuencia principal y obtener el nombre de la estrella.

### Atributos:

- `nombre` (str): El nombre de la estrella.
- `_masa` (float): La masa de la estrella en kilogramos (protegido).
- `_radio` (float): El radio de la estrella en metros (protegido).
- `_temperatura` (float): La temperatura efectiva de la estrella en Kelvin (protegido).
- `_distancia` (float): La distancia de la estrella a la Tierra en parsecs (protegido).
- `_movimiento` (float): El movimiento propio de la estrella en segundos de arco por año (protegido).

### Métodos:

- `luminosidad_total()`: Calcula la luminosidad total de la estrella en vatios.
- `luminosidad_secuencia()`: Calcula la luminosidad de la secuencia principal de la estrella, comparada con el Sol.
- `get_name()`: Devuelve el nombre de la estrella.

## Clase SistemaJerarquico

La clase SistemaJerarquico modela un sistema de estrellas jerárquico y proporciona métodos para operar con ellas.

### Atributos:

- `estrellas` (list): Una lista de objetos de la clase `Estrella` que componen el sistema jerárquico.

### Métodos:

- `sistema_multiple()`: Devuelve una lista con los nombres de las estrellas del sistema jerárquico.
- `estrellas_masa()`: Devuelve una lista de estrellas ordenadas por su masa estelar.
- `letra()`: Imprime los nombres de las estrellas seguidos de letras del alfabeto.
- `estrellas_masa()`: Devuelve una lista de estrellas ordenadas por su masa estelar.

## Clase Planeta

La clase Planeta modela un planeta y proporciona métodos para calcular propiedades como el período de rotación kepleriana.

### Atributos:

- `_anfitriona` (Estrella): La estrella anfitriona alrededor de la cual orbita el planeta.
- `_masa_planeta` (float): La masa del planeta en kilogramos.
- `_radio_planeta` (float): El radio del planeta en metros.
- `_a` (float): El semieje mayor de la órbita del planeta en metros.
- `_i` (float): La inclinación orbital del planeta en grados.
- `_e` (float): La excentricidad orbital del planeta.
- `_w` (float): El argumento del periastron del planeta en grados.

### Métodos:

- `periodo_rotacion()`: Calcula el período de rotación kepleriana del planeta.

## Clase Exoplaneta

La clase Exoplaneta hereda de la clase `Planeta` y agrega métodos para determinar el método de descubrimiento y si el planeta es similar a Tatooine.

### Atributos:

- `_anfitriona` (Estrella): La estrella anfitriona alrededor de la cual orbita el planeta exoplanetario.
- `_masa_planeta` (float): La masa del planeta exoplanetario en kilogramos.
- `_radio_planeta` (float): El radio del planeta exoplanetario en metros.
- `_a` (float): El semieje mayor de la órbita del planeta exoplanetario en metros.
- `_i` (float): La inclinación orbital del planeta exoplanetario en grados.
- `_e` (float): La excentricidad orbital del planeta exoplanetario.
- `_w` (float): El argumento del periastron del planeta exoplanetario en grados.
- `metodo_descubrimiento` (str): El método de descubrimiento del planeta exoplanetario.

### Métodos:

- `periodo_rotacion()`: Calcula el período de rotación kepleriana del planeta exoplanetario.
- `metodo_descubrimiento()`: Devuelve el método de descubrimiento del planeta exoplanetario.
- `similar_Tatooine()`: Determina si el planeta exoplanetario es similar a Tatooine (orbita alrededor de una estrella binaria).
- `parametro_impacto()`: Calcula el parámetro de impacto del planeta exoplanetario (solo si el método de descubrimiento es "Primary Transit").

## Clase Sistema_Planetario

La clase Sistema_Planetario modela un sistema planetario y proporciona métodos para mostrar detalles de los objetos que lo componen.

### Atributos:

- `estrellas` (list): Una lista de objetos de la clase `Estrella` que componen el sistema planetario.
- `planetas` (list): Una lista de objetos de la clase `Planeta` que componen el sistema planetario.
- `sistema_jerarquico` (list): Una lista de objetos de la clase `SistemaJerarquico` que componen el sistema planetario.
- `exoplanetas` (list): Una lista de objetos de la clase `Exoplaneta` que componen el sistema planetario.

### Métodos:

- `__str__()`: Devuelve una representación en cadena del objeto, mostrando el número de estrellas, planetas, sistemas jerárquicos y exoplanetas.
- `mostrar_detalles()`: Imprime los detalles del sistema planetario, incluyendo las propiedades de las estrellas, planetas y exoplanetas.
