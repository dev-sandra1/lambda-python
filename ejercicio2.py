lista = [(1, 2), (3, 1), (5, 4)]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)  # Debería imprimir [(3, 1), (1, 2), (5, 4)]

#ordenar tuplas por el segundo elemento de la tupla