# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:05:12 2022
@author: AnaPov
"""

##
 # Reto #0
 # * EL FAMOSO "FIZZ BUZZ"
 # * Fecha publicación enunciado: 27/12/21
 # * Fecha publicación resolución: 03/01/22
 # * Dificultad: FÁCIL
 # *
 # * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 # * - Múltiplos de 3 por la palabra "fizz".
 # * - Múltiplos de 5 por la palabra "buzz".
 # * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 # *
 # * Información adicional:
 # * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🗓reto-semanal" para preguntas, dudas o prestar ayuda la acomunidad.
 # * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 # *
 # 


rang = range(1, 101, 1)
for i in rang:

    divisible_by_three = i % 3 == 0
    divisible_by_five = i % 5 == 0

    if (divisible_by_three and divisible_by_five):
        print("fizzbuzz")
    elif (divisible_by_five):
        print("buzz")
    elif (divisible_by_three):
         print("fizz")
    else:
        print(i)
