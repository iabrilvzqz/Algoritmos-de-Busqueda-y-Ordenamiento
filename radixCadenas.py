"""	Radix Sort
	Autores:	Hernandez Garcia Luis Angel
				Vazquez Sanchez Ilse Abril
	
	Descripcion: Este programa tiene ligeras modificaciones respecto al Radix Sort para numeros
	ya que nos permite ordenar palabras. Estas se pasan a mayuscula ya que haremos uso del codigo ascii
	de las letras mayusculas para llevar a cabo el ordenamiento.

	A diferencia de los digitos, agregamos un caracter especial a la derecha para que queden todas las 
	palabras de la misma longitud.

"""
import sys
# Funcion que ejecuta el algoritmo de Radix Sort
def radix(l):
	# (1)
	max = 0
	# Encontramos el elemento de mayor longitud en la lista de numeros 
	for i in l:
		if len(i) > max:
			max = len(i)

	# Agregamos 0's a la izquierda de los numeros para que todos tengan la misma longitud
	for i in range(len(l)):
		while len(l[i]) < max:
			l[i] = l[i] + "@"

	# (2) y (3)
	for j in range(max-1,-1,-1): # Se itera por cada digito

		ocr = [[] for i in range(27)] # Lista de listas

		# Cada lista de ocr tendra numeros de acuerdo al valor del digito j
		for i in range(len(l)):
			ocr[ ord(l[i][j]) - 64 ].append(l[i])


		l = [] # Se limpia la lista original para guardar las cadenas ordenadas
		
		# Se guardan las cadenas ordenadas
		for i in range(27):
			l += ocr[i]
	
	return [n.replace("@", "") for n in l] # Se regresa la lista

lista = sys.stdin.readline().replace("\n", "")
lista = [n.upper() for n in lista.split(",")]

print(radix(lista))