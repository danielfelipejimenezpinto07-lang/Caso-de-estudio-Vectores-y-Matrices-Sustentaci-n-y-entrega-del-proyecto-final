import numpy as np

def suma_vectores(v1, v2):
    if len(v1) != len(v2):
        return "Error: los vectores deben tener la misma longitud."
    return np.array(v1) + np.array(v2)

def producto_punto(v1, v2):
    if len(v1) != len(v2):
        return "Error: los vectores deben tener la misma longitud."
    return np.dot(v1, v2)

def suma_matrices(m1, m2):
    matriz1 = np.array(m1)
    matriz2 = np.array(m2)

    if matriz1.shape != matriz2.shape:
        return "Error: las matrices deben tener la misma dimensión."
    return matriz1 + matriz2

def multiplicacion_matrices(m1, m2):
    matriz1 = np.array(m1)
    matriz2 = np.array(m2)

    if matriz1.shape[1] != matriz2.shape[0]:
        return "Error: las columnas de la primera matriz deben ser iguales a las filas de la segunda."
    return np.dot(matriz1, matriz2)

def transpuesta_matriz(m):
    matriz = np.array(m)
    return matriz.T

def determinante_matriz(m):
    matriz = np.array(m)

    if matriz.shape[0] != matriz.shape[1]:
        return "Error: la matriz debe ser cuadrada para calcular el determinante."
    return round(np.linalg.det(matriz), 2)

def menu():
    print("\n=== OPERACIONES CON VECTORES Y MATRICES ===")
    print("1. Suma de vectores")
    print("2. Producto punto")
    print("3. Suma de matrices")
    print("4. Multiplicación de matrices")
    print("5. Transpuesta de una matriz")
    print("6. Determinante de una matriz")
    print("7. Salir")

def ejecutar_programa():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            v1 = [2, 3]
            v2 = [4, 1]
            print("Vector 1:", v1)
            print("Vector 2:", v2)
            print("Resultado:", suma_vectores(v1, v2))

        elif opcion == "2":
            v1 = [1, 2, 3]
            v2 = [4, 5, 6]
            print("Vector 1:", v1)
            print("Vector 2:", v2)
            print("Resultado:", producto_punto(v1, v2))

        elif opcion == "3":
            m1 = [[1, 2], [3, 4]]
            m2 = [[5, 6], [7, 8]]
            print("Matriz 1:", m1)
            print("Matriz 2:", m2)
            print("Resultado:\n", suma_matrices(m1, m2))

        elif opcion == "4":
            m1 = [[1, 2], [3, 4]]
            m2 = [[2, 0], [1, 2]]
            print("Matriz 1:", m1)
            print("Matriz 2:", m2)
            print("Resultado:\n", multiplicacion_matrices(m1, m2))

        elif opcion == "5":
            m = [[1, 2, 3], [4, 5, 6]]
            print("Matriz:", m)
            print("Resultado:\n", transpuesta_matriz(m))

        elif opcion == "6":
            m = [[1, 2], [3, 4]]
            print("Matriz:", m)
            print("Resultado:", determinante_matriz(m))

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

ejecutar_programa()
