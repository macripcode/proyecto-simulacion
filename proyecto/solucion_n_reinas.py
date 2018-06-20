# Algoritmo para solucionar n-reinas usando un algoritmo probabilistico las vegas tipo 2

from math import *
import sys
import random


# # --------Variables----------------->
# # numero de iteraciones realizadas por el algoritmo para encontrar una solución
n_iter_n_queens_vegas = 0
# # variable de parada para el algoritmo
# exito = False
# # contiene la solucion encontrada por el algoritmo, es decir un vector de las reinas y so posicion
# solucion = None
# # --------Termina Variables--------->


# --------Funciones----------------->

# Esta funcion genera un vector con la posicion de n reinas aleatoriamente y verifica si es una solucion valida
# retorna el vector encontrado
def n_queens_vegas(n):
    # Crea un vector con la ubicacion de n reinas en orden aleatorio
    queens = random.sample(range(n), n)

    # verificando por las diagonales en 45 grados
    for i in reversed(range(n)):
        number = queens[i]
        print(number)
        for j in reversed(range(i)):
            number = number-1
            if (number >= 0) & (number <= n-1):
                if(number == queens[j]):
                    return False

    # verificando por las diagonales en 135 grados
    for i in reversed(range(n)):
        number = queens[i]
        print(number)
        print("---------------")
        for j in reversed(range(i)):
            number = number+1
            if (number >= 0) & (number <= n-1):
                if(number == queens[j]):
                    return False

    return queens

# Esta funcion se encarga de llamar a la funcion n_queen_vegas las veces necesarias para encontrar una solucion valida
# retorna el numero de iteraciones realizadas para encontrar la solucion


def maestro_n_queen_vegas(n_queen, exito, solucion, n_iter_n_queens_vegas):
    while exito == False:
        y = n_queens_vegas(n_queen)
        n_iter_n_queens_vegas = n_iter_n_queens_vegas + 1
        solucion = y
        exito = y

    print("La solucion encontrada es: ")
    print(solucion)
    print("El numero de iteraciones necesarias fue: "+str(n_iter_n_queens_vegas))

    return n_iter_n_queens_vegas

# --------Termina Funciones Vegas--------->


# --------Variables----------------->
# Diccionario en donde se van acomodando las n reinas
x = {}
# Vector que contiene la solucion encontrada
queens = []
# Iterador es por defecto 1, ya que es un algoritmo determinista
# n_iter_n_queens = 0
# --------Termina Variables--------->

# --------Funciones----------------->


def place(k, i):
    if (i in x.values()):
        return False
    j = 1
    while(j < k):
        if abs(x[j]-i) == abs(j-k):
            return False
        j += 1
    return True


def clear_future_blocks(k, n):
    for i in range(k, n):
        x[i] = None


def NQueens(k, n):
    iteraciones = 0
    for i in range(0, n):
        clear_future_blocks(k, n)
        if place(k, i):
            x[k] = i
            if (k == n):
                for j in x:
                    queens.append(x[j])
            else:
                iteraciones += 1
                NQueens(k+1, n)
    return iteraciones


def n_queens(n, n_iter_n_queens):
    n_iter_n_queens = NQueens(1, n)
    NQueens(1, n)
    print("La solucion encontrada es: ")
    print(queens)
    print("El numero de iteraciones necesarias fue: "+str(n_iter_n_queens))
    return n_iter_n_queens

# --------Termina Funciones Determinista--------->
