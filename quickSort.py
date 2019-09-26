"""	Quick Sort
	Autores:	Hernández García Luis Angel
				Vázquez Sánchez Ilse Abril

	Basado en la técnica "divide y vencerás". De complejidad O(n log(n)).

	Algoritmo:
	1) Elegir un elemento del arreglo como pivote.
	2) Reubicar los demás elementos de la lista a cada lado del pivote; del lado izquierdo los menores y del derecho los mayores (o viceversa).
	3) Se ubica al pivote en su posición, dividiendo la lista en dos.
	4) Repetir el proceso recursivamente para cada sublista. """

def reacomodo(l, p):
	j = 0 # Variable para controlar la posición del pivote

	# Se acomodan los elementos menores al pivote a la izquierda los mayores se quedan como están
	for i in range(p):
		if l[i] < l[p]:
			aux = l[j]
			l[j] = l[i]
			l[i] = aux
			j += 1

	# Se acomoda al pivote en posición
	aux = l[j]
	l[j] = l[p]
	l[p] = aux

	print(l)

	return [l, j] # Se regresa la lista y la posición del pivote

# Función principal de quick sort. Recibe una lista como parámetro 
def quickSort(l):
	if len(l) <= 1:
		return l

	piv = len(l) - 1 # (1) Se elige al numero en la ultima posición
	r = reacomodo(l, piv) # (2) y (3)
	l = r[0] # Lista con pivote en posición; elementos menores a la izquierda y mayores a la derecha
	piv = r[1] # Nueva posición del pivote

	
	# (4)
	l1 = quickSort(l[:piv])
	l2 = quickSort(l[piv + 1:])

	l1.append(l[piv])

	return l1 + l2

lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]

print(lista)
print(quickSort(lista))