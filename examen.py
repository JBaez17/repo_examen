# -*- coding: utf-8 -*-
import random


def valores_vistos(num_iteraciones):
    tiradas = []
    aparecidos = set()
    for i in range(num_iteraciones):
        dado1 = random.randrange(1, 7, 2)
        dado2 = random.randrange(1, 7, 2)
        suma = dado1 + dado2
        tiradas.append(suma)
        aparecidos.add(suma)
    apariciones = {}
    for num_aparecidos in aparecidos:
        cont = 0
        for num in tiradas:
            if num_aparecidos == num:
                cont += 1
        apariciones[str(num_aparecidos)] = cont
    return apariciones


def realizar_tirada():
    cantidad_iteraciones = input("Cuantas iteraciones se deben realizar?")
    apariciones = valores_vistos(cantidad_iteraciones)
    for key in apariciones:
        print "{0} aparecio {1} veces".format(key, apariciones[key])


realizar_tirada()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
