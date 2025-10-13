#Ejercicio 1:
#def hola_amiga():
#    print("Hola amiga!!")
#    return
#
#hola_amiga()

#Ejercicio 2:
#def saludo(nombre):
#    print(f"Hola {nombre}!!")
#    return
#
#saludo("Pepe")
#saludo("Adrián")


#Ejercicio 3:
#def factorial(num):
#    result = 1
#    for i in range(num):
#        result *= (num - i)
#    return print(result)
#factorial(5)


#Ejercicio 4:
#def factura_iva(monto, iva = 21):
#    return monto + monto*iva/100
#print(factura_iva(1000,10))
#print(factura_iva(1000))


#Ejercicio 5:
#def area_circular(r,h=0):
#    pi = 3.1415
#    return 2*pi*r*h + pi*r**2
#print(area_circular(3,5))
#print(area_circular(3))


#Ejercicio 6:
#def media(lista_n):
#    return sum(lista_n) / len(lista_n)
#
#print(media([1, 2, 3, 4, 5]))
#print(media([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


#Ejercicio 7:
#def cuadrado(lista_num):
#    lista_cuadrado = []
#    for i in lista_num:
#        lista_cuadrado.append(i**2)
#    return lista_cuadrado
#print(cuadrado([1, 2, 3, 4, 5]))
#print(cuadrado([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


#Ejercicio 8:
#def media_varianza_desvtip(lista_num):
#    media = sum(lista_num) / len(lista_num)
#    varianza = 0
#    for i in range(len(lista_num)):
#        varianza += ((i - media)**2)/(len(lista_num)-1)
#    desv_tip = varianza**1/2
#    return media, varianza, desv_tip
#
#print(media_varianza_desvtip([1, 2, 3, 4, 5]))
#print(media_varianza_desvtip([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


#Ejercicio 9:
def mcd(a,b):
    rest = 0
    while(b > 0):
        rest = b
        b = a % b
        a = rest
    return a

def mcm(a, b):
    if a > b:
        mayor = a
    else:
        mayor = b
    while (mayor % a != 0) or (mayor % b != 0):
        mayor += 1
    return mayor

print(mcd(24,36))
print(mcm(24,36))