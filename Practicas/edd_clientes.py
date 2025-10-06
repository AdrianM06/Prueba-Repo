edd_clientes = {
    31758845: {
        "nombre": "Adrián",
        "dirección": "Caracas",
        "teléfono": 4127398470,
        "correo": "aeidhrym@gmail.com",
        "preferente": True,
    },
    
}

def agregar_cliente(edd_clientes):
  nif = int(input("Ingresa tu NIF: "))
  nombre = input("Ingresa tu nombre: ")
  direccion = input("Ingresa tu direccion: ")
  telefono = int(input("Ingresa tu telefono: "))
  correo = input("Ingresa tu correo: ")
  preferente = input("Indica si es cliente preferente (s/n): ")
  if preferente == "s":
    preferente = True
  else:
    preferente = False
  edd_clientes[nif] = {
      "nombre": nombre,
       "dirección": direccion,
      "teléfono": telefono,
      "correo": correo,
      "preferente": preferente,
  }

def eliminar_cliente(edd_clientes):
  nif = int(input("\nEscribre el NIF del cliente a eliminar: "))
  if nif in edd_clientes:
    print(f"\nCliente con NIF {nif} eliminado")
    del edd_clientes[nif]
  else:
    print(f"\nCliente con NIF {nif} no encontrado, no se puede eliminar")

def mostrar_cliente(edd_clientes):
  nif = int(input("Escribre el NIF del cliente que quieres mostar: "))
  if nif in edd_clientes:
    cliente = edd_clientes[nif]
    mostrar_preferente = "No"
    if cliente["preferente"]:
      mostrar_preferente = "Sí"
    print(f'\n----{cliente["nombre"]}----')
    print(f'Dirección: {cliente["dirección"]}')
    print(f'Teléfono: {cliente["teléfono"]}')
    print(f'Correo: {cliente["correo"]}')
    print(f'¿El cliente es preferente? {mostrar_preferente}')
  else:
    print(f"\nCliente con NIF {nif} no encontrado, no se puede mostrar")

def mostrar_todos_clientes(edd_clientes):
  for cliente in edd_clientes:
    print(f'\n----{edd_clientes[cliente]["nombre"]}----')
    print(f'Dirección: {edd_clientes[cliente]["dirección"]}')
    print(f'Teléfono: {edd_clientes[cliente]["teléfono"]}')
    print(f'Correo: {edd_clientes[cliente]["correo"]}')

def mostar_clientes_preferidos(edd_clientes):
  for nif, cliente in edd_clientes.items():
    if cliente["preferente"] == True:
     print(f"Nif: {nif}, Nombre: {cliente["nombre"]}")

print("----Bienvenidos a la BDD de los clientes de la empresa no se que----\n\n")

while True:
  print("\nMenú de opciones:\n" \
        "1. Añadir cliente\n" \
        "2. Eliminar cliente\n" \
        "3. Mostrar cliente\n" \
        "4. Lista de todos los clientes\n" \
        "5. Lista de clientes preferidos\n" \
        "6. Terminar\n")
  opcion = input("Selecciona una opción\n-->")

  if opcion == "1":
    agregar_cliente(edd_clientes)
  elif opcion == "2":
    eliminar_cliente(edd_clientes)
  elif opcion == "3":
    mostrar_cliente(edd_clientes)
  elif opcion == "4":
    mostrar_todos_clientes(edd_clientes)
  elif opcion == "5":
    mostar_clientes_preferidos(edd_clientes)
  elif opcion == "6":
    print("\nGracias por usar el programa")
    break
  else:
    print("Error. Escoge una de las opciones disponibles")
