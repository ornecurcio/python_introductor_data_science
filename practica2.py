# -*- coding: utf-8 -*-
"""practica2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nJ6FjiI5h1JI-2puMk-ozVH2JjgzQEoL

# Programación para Analisis de datos
## Práctica 2: Introducción a Python II
## Índice:

1. [Condicionales](#Ejercicios-con-condicionales)
2. [Ciclos](#Ejercicios-con-Ciclos)
3. [Funciones](#Ejercicios-con-funciones)
4. [Ejercicios Extras](#Ejercicios-Extras)


<b>Nota:</b>
Esta práctica contiene ejercicios que cubren los diferentes temas vistos en la intrudicción de Python como lenguaje de programación. En las celdas de código, donde vea $<CODIGO>$, debera completar con el código que resuelva lo que se pide. En la mayoria de los ejercicios se debera recurrir a las referencias técnicas para resolver los enunciados. Bajo cada seccion esta el link a las referencias oficiales de python, sin embargo no dude en usar otras fuentes.

<hr>

## Ejercicios con condicionales</b>
referencias: https://www.w3schools.com/python/python_conditions.asp

1. Programa el comportamiento de un modulo de un numero, es decir, si el numero es negativo le cambia el signo. Si el numero es positivo lo deja tal como esta
"""



"""2. El siguiente codigo imprime por pantalla si un numero es divisible por otro. Este codigo tiene un error, descubralo y arreglelo."""

a = 7
b = 2
if a%b == 0:
    print(a,'divide a ',b)
else:
    print(a,'NO divide a ',b)

"""3. Escriba un código que imprima por pantalla si un numero es divisible por 3 y por 2. Debe imprimir todas las condiciones posibles, es decir, si es divisible por uno y no por el otro."""



"""4. Escriba un código para dado un entero del 1 al 7 imprima el dia de la semana. Ahora escriba tambien una solución que resuelva lo mismo pero no use ningun if"""



"""## Ejercicios con Ciclos
referencias: https://www.w3schools.com/python/python_for_loops.asp

5. Escriba un codigo que imprima los numeros del uno al 10 un numero por linea.
"""



"""6. Imprima lo mismo del ejercicio anterior pero usando for y range.


"""



"""7. Guarde en una lista todos los numeros menores a 100 que sean pares


"""

numeros_pares_menores_a_100 = []
for i in range(<CODIGO>):
    # Chequeamos si el numero que estoy usando para iterar es par o no
    if <CODIGO>:
        # Si estoy aca es porque el numero es par, entonces lo agrego a la lista numeros_pares_menores_a_100
        <CODIGO>
        
# Imprimo los numeros pares menores a 100 
print(numeros_pares_menores_a_100)

"""8. Calcule todos los divisores de un número $n$. Pruebe distintos valores para la variable $n$. Pruebe escribirlos con un $while$ y con un $for$


"""

n = 123
lista_de_divisores = []
<CODIGO>
# Imprimo los divisores de a 1 
print(lista_de_divisores)

"""9. Imprima por pantalla todos los numeros primos menos a $n$, pruebe con diferentes valores de $n$


"""



"""## Ejercicios con funciones
Algunos de los siguientes ejercicios fueron tomados de diferentes recursos como: 
* https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
* https://github.com/darkprinx/100-plus-Python-programming-exercises-extended
* https://projecteuler.net/

10. Encapsule las funciones de los ejercicios 8 y 9 de modo que tomen el parámetro $n$. Experimente con diferentes parámetros
"""

# Funcion lista de divisores
def lista_de_divisores(n):
    <CODIGO>

# Funcion codigo numeros primos menores a n
<CODIGO>

"""11. Escriba una funcion que calcule todos los numeros divisibles por 7 pero no multiplos de 5 entre 1000 y 5000.

La funcion debe devolver una lista con estos numeros
Hints: Puede usar la funcion range(desde,hasta)

12. Haga una función que calcule el factorial de un numero $n$
"""



"""13. Escriba una función que devuelva un diccionario donde las claves sean los numeros del 1 al $n$ (con $n$ parametro de la función) y en el significado de cada clave este guardado el cuadrado de ese numero.

Por ejemplo si a la función le entra un 4 la funcion debe devolver {1:1,2:4,3:9,4:16}
"""



"""14. Escriba una función que tome una lista de enteros y devuelva una lista de lista, donde cada lista contenga los divisores del numero correspondiente.

Por ejemplo si función toma como entrada [3,6,12,11], la salida debe ser [[1,3],[1,2,3,6],[1,2,3,6,12],[1,11]]
"""



"""15. Escriba una función que tome un numero entero y devuelva una lista con tuplas con los numeros primos que lo dividen y la cantidad de veces que el numero primo lo divide.

Por ejemplo, si entra el número 2223000 la función debe devolver: [(2,3),(3,2),(13,1),(19,1)] pues $2^3 \times 3^2 \times 13^1 \times 19^1 = 2223000$
"""

"""
Esto es una tupla en python, puede tener una cantidad fija 
pero arbitraria de elementos (es decir puede ser tan grande
como se quiera pero no puede mutar)"""
tupla = (3,6)

"""16. Un número palíndromo se lee del derecho y el reves de la misma forma. El palindrome hecho por el producto de dos numeros de dos digitos mas grande es 9009 pues es producto de $91*99$

Escriba un código para crear el palindromo más grande hecho por el pruducto de 2 numeros de 3 digitos

Nota: Este ejercicio fue tomado de: https://projecteuler.net/problem=4

"""



"""17. Escriba una función que devuelve el $i-esimo$ número de la sucesión de Fibonacci  (https://en.wikipedia.org/wiki/Fibonacci_number)"""



"""## Ejercicios Extras
18. Registrese en https://projecteuler.net/ y complete todos los ejercicios que quiera en orden
"""

