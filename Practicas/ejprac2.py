#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#for asignatura in asignaturas:
#    print(asignatura)

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#for asignatura in asignaturas:
#    print(f"Yo estudio {asignatura}")

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#notas = []
#for asignatura in asignaturas:
#    nota = input(f"Ingrese la nota que obtuvo en: {asignatura}\n--> ")
#    notas.append(nota)
#for i in range(len(asignaturas)):
#    print(f"La nota obtenida en {asignaturas[i]} es: {notas[i]}")

#loteria = []
#for i in range(7):
#    loteria.append(input(f"Ingrese el número {i+1} de la lotería primitiva:\n--> "))
#loteria.sort()
#print(f"Los número ganadores de la lotería primitiva son: {loteria}")

#lista = [1,2,3,4,5,6,7,8,9,10]
#lista.reverse()
#print(lista)

#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#asignaturas_pasadas = []
#for asignatura in asignaturas:
#    nota = input(f"Ingrese la nota quye obtuvo en {asignatura}\n--> ")
#    while not nota.isnumeric:
#        nota = input(f"Error. Ingrese un valor válido para la nota:\n--> ")
#    if int(nota) >= 10:
#        asignaturas_pasadas.append(asignatura)
#for asignatura_pasada in asignaturas_pasadas:
#    asignaturas.remove(asignatura_pasada)
#print(f"Las asignaturas que has raspado son: {asignaturas}")

#abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#for i in range(len((abecedario)), 1, -1):
#    if i % 3 == 0:
#        abecedario.pop(i-1)
#print(abecedario)

#palabra = input("Escriba una palabra:\n--> ")
#palabra_al_reves = palabra
#palabra = list(palabra)
#palabra_al_reves = list (palabra_al_reves)
#palabra_al_reves.reverse()
#if palabra == palabra_al_reves:
#    print("La palabra es palíndroma.")
#else:
#    print("La palabra no es palíndroma.")

#palabra = input("Escribe una palabra:\n--> ")
#vocales  = ["a","e","i","o","u"]
#for vocal in vocales:
#    veces = 0
#    for letra in palabra:
#        if letra == vocal:
#            veces += 1
#    print(f"La palabra: {palabra} contiene la vocal: {vocal} {veces} veces.")


#precios = [50,75,46,22,80,65,8]
#min = max = precios[0]
#for precio in precios:
#    if precio < min:
#        min = precio
#    if precio > max:
#        max = precio
#print(f"El mayor de los precios es: {max}")
#print(f"El menor de los precios es: {min}")

#vector_a = (1,2,3)
#vector_b = (-1,0,2)
#producto_escalar = 0
#for i in range(len(vector_a)):
#    producto_escalar += vector_a[i] * vector_b[i]
#print(f"El producto escalar de {vector_a} con {vector_b} es: {producto_escalar}")


#a = ((1, 2, 3),
#     (4, 5, 6))
#b = ((-1, 0),
#     (0, 1),
#     (1,1))
#resultado = [[0,0],
#             [0,0]]
#for i in range(len(a)):
#    for j in range(len(b[0])):
#        for k in range(len(b)):
#            resultado[i][j] += a[i][k] * b[k][j]
#for i in range(len(resultado)):
#    resultado[i]= tuple(resultado[i])
#resultado = tuple(resultado)
#for i in range(len(resultado)):
#    print(resultado[i])

#numeros = input("Ingrese una secuencia de números separados por comas:\n--> ")
#numeros = numeros.split(",")
#n = len(numeros)
#for i in (range(n)):
#    numeros[i] = int(numeros[i])
#numeros = tuple(numeros)
#suma = 0
#suma_cuadrada = 0
#for i in numeros:
#    suma += i
#promedio = suma / n 
#for i in numeros:
#    suma_cuadrada += (i - promedio)
#desv_estandar = (suma_cuadrada**2/promedio - 1)**0.5
#print(f"El promedio es: {promedio} y la desviación esntándar es: {desv_estandar}")

## Ejercicios de diccionarios

#simbolos = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#moneda = input("introduce una moneda:\n--> ")
#print(simbolos.get(moneda.title(), "La moneda no está"))

#usuario = {}
#usuario["nombre"] = input("Introduce tu nombre:\n--> ")
#usuario["edad"] = input("Introduce tu edad:\n--> ")
#usuario["direccion"] =input("Introduce tu direccion:\n--> ")
#usuario["telefono"] = input("Introduce tu teléfono:\n--> ")
#print(f" {usuario["nombre"]} tiene {usuario["edad"]} años, vive en {usuario["direccion"]} y su número de teléfono es {usuario["telefono"]}.")

#verduleria = {"platano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}
#fruta = input("Indique cual fruta desea:\n--> ")
#kilos = float(input("Indique cuántos kilos va a llevar:\n--> "))
#if fruta in verduleria:
#    print(f"El costo de {kilos} kg de {fruta} es de {verduleria[fruta]*kilos}")
#else:
#    print(f"Disculpe, {fruta} no está disponible")

#meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
#fecha = input("Introduce una fecha en el formato dd/mm/aaaa:\n--> ")
#fecha = fecha.split("/")
#print(f"{fecha[0]} de {meses[int(fecha[1])]} del {fecha[2]}")

#plan = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
#creditos = 0
#for asignatura,credito in plan.items():
#    print(f"La asignatura {asignatura} tiene {credito} creditos.")
#    creditos += credito
#print(f"El total de créditos de todas las asignaturas es de: {creditos}")


#usuario = {}
#continuar = True
#while continuar:
#    clave = input("¿Qué dato desea agregar:\n--> ")
#    valor = input(f"Indique cuál es su {clave}:\n--> ")
#    usuario[clave] = valor
#    print(usuario)
#    continuar = input("Desea añadir más información (si/no):\n--> ") == "si"
#    print(continuar)
    
#cesta = {}
#continuar = True
#while continuar:
#    articulo = input("Introduzca el artículo a comprar:\n--> ")
#    precio = float(input(f"Introduzca el precio de {articulo}:\n--> "))
#    cesta[articulo] = precio
#    continuar = input("¿Desea agregar más artículos a la bolsa? (si/no):\n--> ") == "si"
#total = 0
#print("---Lista de compras---")
#for i,j in cesta.items():
#    print(f"{i} tiene un precio de {j}$")
#    total += j
#print(f"El precio total fue: {total}$")

#diccionario = {}
#palabras = input("Ingrese una lista de palabras separadas por comas tal que: (palabra-1: traducción-1), (palabra-2: traducción-2)... \n--> ")
#for i in palabras.split(","):
#    palabra, traducción = i.split(":")
#    diccionario[palabra] = traducción
#frase = input("Introduce una frase que contenga palabras del diccionario:\n--> ")
#for i in frase.split():
#    if i in diccionario:
#        print(diccionario[i], end = " ")
#    else:
#        print(i, end = " ")


#facturas = {}
#cant_cobrada = 0
#cant_pendiente = 0
#while True:
#    print("---Bienvenido a la gestión de factura de cobro de la empresa---\n¿En qué puedo ayudarte?\n")
#    print(f"Se ha pagado: {cant_cobrada}$ y queda pendiente: {cant_pendiente}$\n")
#    opcion = input("Deseas:\n--> 1.Añadir una nueva factura.\n--> 2.Pagar una factura existente.\n--> 3.Salir del programa.\n--> ")
#    if opcion == "1":
#        num_factura = input("\nIndique el número de la factura a añadir:\n-->")
#        coste = float(input(f"Indique el coste de la factura num°{num_factura}:\n--> "))
#        facturas[num_factura] = coste
#        cant_pendiente += coste
#        print(facturas)
#    elif opcion == "2":
#        num_factura = input("\nIndique el número de la factura a pagar:\n-->")
#        cant_cobrada += facturas[num_factura]
#        cant_pendiente -= facturas[num_factura]
#        facturas.pop(num_factura)
#        print(facturas)
#    elif opcion == "3":
#        print("¡¡Gracias, vuelva pronto!!")
#        break
#    else:
#        print("\nError, debe eligir una opción válida.\n")
#        continue


texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
lista_texto = texto.split('\n')
directorio = {}
lista_clientes = lista_texto[0].split(';')
for i in lista_texto[1:]:
    cliente = {}
    lista_aux = i.split(';')
    for j in range(1,len(lista_clientes)):
        if lista_clientes[j] == "descuento":
            lista_aux[j] = float(lista_aux[j])
        cliente[lista_clientes[j]] = lista_aux[j]
    directorio[lista_aux[0]] = cliente
print(directorio)


datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
lista_clientes = datos_clientes.split('\n')
directorio = {}
lista_campos = lista_clientes[0].split(';') 
for i in lista_clientes[1:]:
    cliente = {}
    lista_info = i.split(';') 
    for j in range(1,len(lista_campos)):
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    directorio[lista_info[0]] = cliente
print(directorio)