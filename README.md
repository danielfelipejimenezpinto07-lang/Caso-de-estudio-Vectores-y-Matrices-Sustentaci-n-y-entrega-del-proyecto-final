# Caso-de-estudio-Vectores-y-Matrices-Sustentación-y-entrega-del-proyecto-final

## Descripción del proyecto

Este proyecto presenta la solución de un caso de estudio relacionado con operaciones básicas de vectores y matrices mediante el lenguaje de programación Python.

El programa permite realizar diferentes operaciones matemáticas, validando previamente las condiciones necesarias para que cada operación pueda ejecutarse correctamente. De esta manera, se busca aplicar los conocimientos vistos durante el curso y demostrar el uso de estructuras de datos, condicionales, funciones y validaciones dentro de un programa funcional.

## Objetivo del proyecto

Desarrollar una solución en Python que permita realizar operaciones con vectores y matrices de forma clara, ordenada y confiable, evitando errores manuales y validando las condiciones requeridas para cada cálculo.

## Funcionalidades del programa

El programa permite realizar las siguientes operaciones:

* Suma de vectores.
* Producto punto entre vectores.
* Suma de matrices.
* Multiplicación de matrices.
* Transpuesta de una matriz.
* Determinante de una matriz.
* Validación de dimensiones y condiciones antes de ejecutar cada operación.

## Tecnologías utilizadas

* Python 3
* NumPy
* Git
* GitHub
* BPMN 2.0 para el modelado del proceso

## Estructura del repositorio

```text
caso-vectores-matrices/
│
├── main.py
├── README.md
├── INFORME TECNICO PROYECTO FINAL.docx
├── Diagrama procesos usando BPMN 2.0.png
│
└── Pruebas escritorio.docx
    ├── prueba_1_suma_vectores.png
    ├── prueba_2_producto_punto.png
    └── prueba_3_multiplicacion_matrices.png
```

## Descripción de los archivos

| Archivo o carpeta      | Descripción                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `main.py`              | Contiene el código principal del programa desarrollado en Python.                       |
| `README.md`            | Documento de presentación del proyecto en el repositorio.                               |
| `informe_tecnico.docx` | Informe técnico del caso de estudio.                                                    |
| `diagrama_bpmn.png`    | Diagrama de procesos elaborado bajo BPMN 2.0.                                           |
| `pruebas_escritorio/`  | Carpeta que contiene las imágenes de las pruebas de escritorio del código en ejecución. |

## Instalación y ejecución

Para ejecutar el proyecto, se debe tener instalado Python en el computador.

También se debe instalar la librería NumPy con el siguiente comando:

```bash
pip install numpy
```

Luego, se ejecuta el archivo principal:

```bash
python main.py
```

## Explicación general de la solución

El programa funciona mediante un menú de opciones. El usuario selecciona la operación que desea realizar y el sistema ejecuta la función correspondiente.

Antes de realizar cada operación, el programa valida que los datos cumplan las condiciones necesarias. Por ejemplo, para sumar dos vectores, ambos deben tener la misma longitud; para multiplicar matrices, el número de columnas de la primera matriz debe coincidir con el número de filas de la segunda.

Si las condiciones se cumplen, el programa muestra el resultado. Si no se cumplen, se genera un mensaje de error indicando por qué no se puede realizar la operación.

## Funciones principales

### Suma de vectores

Permite sumar dos vectores componente a componente, siempre que ambos tengan la misma longitud.

### Producto punto

Calcula el producto punto entre dos vectores, validando que tengan la misma cantidad de elementos.

### Suma de matrices

Suma dos matrices siempre que tengan la misma dimensión.

### Multiplicación de matrices

Multiplica dos matrices verificando que las columnas de la primera matriz coincidan con las filas de la segunda matriz.

### Transpuesta de una matriz

Convierte las filas de una matriz en columnas y las columnas en filas.

### Determinante de una matriz

Calcula el determinante únicamente si la matriz es cuadrada.

## Pruebas de escritorio

Se realizaron pruebas de escritorio para validar el funcionamiento del programa. Las pruebas verifican que los resultados obtenidos coincidan con los resultados esperados.

Pruebas realizadas:

1. Suma de vectores.
2. Producto punto.
3. Multiplicación de matrices.

Las imágenes de estas pruebas se encuentran en la carpeta `pruebas_escritorio`.

## Diagrama BPMN 2.0

El proceso del programa fue representado mediante un diagrama BPMN 2.0, donde se muestra el flujo general desde la selección de una operación hasta la validación de datos y entrega del resultado.

El diagrama se encuentra en el archivo:

```text
diagrama_bpmn.png
```

## Manejo de ramas

Para el desarrollo del proyecto se propone trabajar con las siguientes ramas:

* `main`: rama principal del repositorio.
* `develop`: rama de integración del proyecto.


Ejemplo:

```text
main
develop

```

Cada integrante realiza sus aportes en su propia rama y posteriormente se integran los cambios en la rama `develop`.

## Realizado por : Daniel Jimenez Pinto y valeri Sofia Espitia Rodriguez

## Conclusión

Este proyecto permitió aplicar conocimientos de programación, lógica matemática y validación de condiciones mediante Python. La solución desarrollada facilita el trabajo con vectores y matrices, reduce errores en los cálculos y permite representar el proceso de forma clara mediante BPMN 2.0 y pruebas de escritorio.

## Referencias

NumPy Developers. (2024). *NumPy documentation*. https://numpy.org/doc/

Python Software Foundation. (2024). *Python documentation*. https://docs.python.org/3/

Object Management Group. (2011). *Business Process Model and Notation BPMN Version 2.0*. https://www.omg.org/spec/BPMN/2.0/

