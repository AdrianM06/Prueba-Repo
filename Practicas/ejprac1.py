#name = input("Tell me your name:\n--> ")
#print(f"Hello {name}!!")

#print(((3 + 2) / (2 * 5))**2)

#num_hours = input("Tell me the number of hours you worked:\n--> ")
#num_pay = input("Tell me the cost per hour:\n--> ")
#while not (num_hours.isdigit() and num_pay.isdigit()):
#    num_hours = input("Error. Please, tell me the number of hours you worked:\n--> ")
#    num_pay = input("Error. Please, tell me the cost per hour:\n--> ")
#pay_hours = float(num_hours) * float(num_pay)
#print(f"Your total pay of your {num_hours} hour(s) is {pay_hours} dolars.")

#name = input("Please, tell me your complete name:\n--> ")
#print(name.title())
#print(name.lower())
#print(name.upper())

#name = input("Please, tell me your complete name:\n--> ")
#print(f"{name} has {len(name)} letter(s)")

#tel = input("Dime el numero de telefono:\n--> ")
#print(f"El numero a llamar es: {tel[4:-3]}")

#phrase = input("Escriba una frase cualquiera:\n--> ")
#print(phrase[::-1])

#cesta = input("Introduzca los elementos de la cesta separada por comas:\n--> ")
#print(f"Los elementos de la cesta son: \n{cesta.replace(",","\n")}")

#nombre = input("Ingrese el nombre del producto:\n--> ")
#precio = float(input("Ingrese el oprecio del producto:\n--> "))
#cantidad = int(input("Ingrese las cantidades del producto:\n--> "))
#print(f"{nombre}, de precio: {precio}$ y valor total de: {precio*cantidad}")

#pword = "gokussj"
#ver = input("Por favor, introduzca la contraseña, no se preocupe por las mayúsculas:\n--> ")
#if pword == ver.lower():
#    print("La contraseña es correcta")
#else:
#    print("La contraseña es incorrecta")

#age = input("Dime tu edad:\n--> ")
#income = input("Dime tus ingresos:\n--> ")
#if int(age) > 16 and int(income) >= 1000:
#    print("Tienes que tributar")
#else:
#    print("No tienes que tributar")

#name = input("Dime tu nombre:\n-->")
#gender = input("Dime tu género (H/M):\n-->")
#if (name.lower() < "m" and gender == "M") or (name.lower() > "n" and gender == "H"):
#    print("Perteneces al grupo 'A'")
#else:
#    print("Perteneces al grupo 'B'")

#print("¡¡Bienvenido a la sala de juegos!!\nEl precio de las entradas es el siguiente:\n--> Si eres mayor de edad = 10$\n--> Si estas entre 4 y 18 años = 5$\n--> Si tienes menos de 4 años = gratis!!")
#age = input("Por favor, dime tu edad:\n--> ")
#if int(age) < 0 or int(age) > 100:
#    age = input("Error, introduce una edad válida:\n--> ")
#if int(age) >= 18:
#    print("El precio que debes pagar es de 10$")
#elif int(age) >= 4 and int(age) < 18:
#    print("El precio que debes pagar es de 5$")
#else:
#    print("No debes pagar nada")

#num = input("Please, enter a int positive number:\n--> ")
#while not num.isnumeric():
#    num = input("Error, please, enter a int positive number:\n--> ")
#if int(num) < 0:
#    num = input("Please, enter a int positive number:\n--> ")
#for i in range(num,-1,-1):
#    print(int(num)-int(i))

#lista = [1,2,3,4,5,6,7,8,9,10]
#lista.reverse()
#print(lista)

lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(lista)):
    if i % 3 == 0:
        lista.pop(i-1)
print(lista)