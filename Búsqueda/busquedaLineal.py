def busLineal(l, x):
	for i in range(0, len(l) // 2 + 1):
		if len(l) > 0:
			if l[0] == x:
				return l[0]
			elif l[len(l) - 1] == x:
				return l[len(l) - 1]
			else:
				l = l[1:len(l) - 1]

	return None

lista = [2, 5,2,67, 6,3,88, 2]

resultado = busLineal(lista, 88)

print(resultado)