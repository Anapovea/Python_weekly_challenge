"""
Created on Mon Jan  3 21:34:02 2022
@author: Ana Povea
"""
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🗓reto-semanal" para preguntas, dudas o prestar ayuda la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.#  
#   Ejemplo:    s1 = "sad"
#               s2 = "asd"
#               The strings are anagrams.

word_1 = input("Introduce word 1:")
word_2 = input("Introduce word 2:")

#Function definition
def function_anagram (word_1, word_2):
  if (word_1==word_2):
      print("They are not anagrams.")
  elif (sorted(word_1)==sorted(word_2)):
      print("They are anagrams.")
  else:
      print("They are not anagrams.")
  return None

result= function_anagram(word_1, word_2)
print(result)


# print("Sorted List returned word_1 :")
# print(sorted(word_1))
# print("Sorted List returned word_2:")
# print(sorted(word_2))

