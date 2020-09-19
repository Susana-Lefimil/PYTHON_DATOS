archivo = open("base_de_datos_de_clientes.csv")

arch_lineas = archivo.readlines()

archivo.close()

numero_de_clientes = len(arch_lineas)

matriz_de_datos = []

for linea in arch_lineas:
	linea = linea.strip()
	fila = linea.split(";")
	matriz_de_datos.append(fila)

print(matriz_de_datos)
for fila in matriz_de_datos:
	rut_cliente = fila[0]
	fila[0] = rut_cliente[5:len(rut_cliente)]


print(matriz_de_datos)
