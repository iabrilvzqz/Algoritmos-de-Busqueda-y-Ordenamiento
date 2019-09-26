"""	Radix Sort
	Autor:	Vázquez Sánchez Ilse Abril
	
	Este algoritmo realiza el ordenamiento procesando los dígitos de los números
	de forma individual. Para este caso se uso la versión LSD (Least Significant Digit).
	
	Algoritmo:
	1) Asegurarse que todos los números tengan el mismo número de dígitos (se pueden añadir 0's a la izquierda).
	2) Ordenar los numeros por el dígito elegido (iniciando con el menos significativo)
	3) Si quedan dígitos regresar al punto 2 con el siguiente dígito en caso contrario termina el algortimo. """

import random
# Función que ejecuta el algoritmo de Radix Sort
def radix(l):
	# (1)
	max = 0
	# Encontramos el elemento de mayor longitud en la lista de números 
	for i in l:
		if len(i) > max:
			max = len(i)

	# Agregamos 0's a la izquierda de los números para que todos tengan la misma longitud
	for i in range(len(l)):
		while len(l[i]) < max:
			l[i] = "0"+l[i]
	print(l)

	# (2) y (3)
	for j in range(max-1,-1,-1): # Se itera por cada dígito

		ocr = [[] for i in range(10)] # Lista de listas

		# Cada lista de ocr tendrá numeros de acuerdo al valor del digito j
		for i in range(len(l)):
			ocr[int(l[i][j])].append(l[i])


		l = [] # Se limpia la lista original para guardar los números ordenados
		
		# Se guardan los numeros ordenados
		for i in range(10):
			l += ocr[i]
	
	return [int(n) for n in l] # Se regresa la lista realizando cast a enteros

lista = [str(random.randint(0,200)) for x in range(6)]
print(lista)

lista = radix(lista)
print(lista)