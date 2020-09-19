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
for fila in matriz_de_datos:
	guion=fila[3]
	fila[3] = guion.replace("-","")
	
print(matriz_de_datos)
for fila in matriz_de_datos:
	fecha = fila[3]
	fecha_lista = fecha.split("/")
	edad = 2018 - int(fecha_lista[0])
	fila[4]=str(edad)
#Segun las instrucciones puse el año 2018


archivo_final = open("clientes_limpio.csv","w")



for fila in matriz_de_datos:
	fila_para_escribir = ""

	for i in range(0,len(fila)):
		if i == len(fila)-1:
			fila_para_escribir += fila[i]
		else:
			fila_para_escribir += fila[i] + ";"

	fila_para_escribir += "\n"

       
       

	archivo_final.write(fila_para_escribir)



archivo_final.close()








 
