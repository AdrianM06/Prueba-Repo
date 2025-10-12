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

vector_a = (1,2,3)
vector_b = (-1,0,2)
producto_escalar = 0
for i in range(len(vector_a)):
    producto_escalar += vector_a[i] * vector_b[i]
print(f"El producto escalar de {vector_a} con {vector_b} es: {producto_escalar}")

