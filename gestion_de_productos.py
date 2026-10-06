#Alumno: Milagros Luna Figueroa
#Pre-Entrega


productos = []

def pedirTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: Este campo no puede estar vacio")
        else:
            return texto

def pedirPrecio(mensaje):
    print("estoy usando pedirPrecio")
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("Error: Solo se puede ingresar numeros enteros, sin centavos ni simbolos.")
        elif int(entrada) <= 0:
            print("Error: el precio debe ser mayor a 0.")
        else:
            return int(entrada)

def pedirCategoria(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: Este campo no puede estar vacio")
        elif texto.isdigit():
            print("Error: La categoría no puede ser solo un número. Describilo.")
        else:
            return texto

def agregarProducto():
    print("\n--- Agregar producto ---")
    nombre = pedirTexto("Nombre: ")
    categoria = pedirCategoria("Categoría: ")
    precio = pedirPrecio("Precio (sin centavos): ")

    productos.append([nombre, categoria, precio])
    print(f"Producto '{nombre}' agregado correctamente.")

def mostrarProductos():
    print("\n**** Productos Registrados ****")
    if len(productos) == 0:
        print("No hay productos registrados hasta el momento.")
        return
    for i in range(len(productos)):
        Nombre,Categoria,Precio = productos[i]
        print(f"{i + 1}. Nombre: {Nombre} | Categoría: {Categoria} | Precio: ${Precio}")

def buscarProductos():
    print("\n**** Buscar Productos ****")
    if len(productos) == 0:
         print("No hay productos registrados.")
         return

    busqueda = pedirTexto("Nombre a buscar: ").lower()
    encontrados = 0

    for i in range(len(productos)):
        nombre, categoria, precio = productos[i]
        if busqueda in nombre.lower():
            print(f"{i + 1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron resultados.")

def eliminarProducto():
    print("\n**** Eliminar Producto ****")
    if len(productos) == 0:
        print("No existen producto a eliminar")
        return

    mostrarProductos()

    while True:
        entrada = input("\nNúmero del producto a eliminar: ").strip()
        if not entrada.isdigit():
            print("Error: ingresá un número válido.")
        elif int(entrada) < 1 or int(entrada) > len(productos):
            print(f"Error: elegí un número entre 1 y {len(productos)}.")
        else:
            eliminado = productos.pop(int(entrada) - 1)
            print(f"Producto '{eliminado[0]}' eliminado correctamente.")
            break

def menuDeInicio():
    print("\nSistema de gestión básica de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

# Programa principal
opcion = ""
while opcion != "5":
    menuDeInicio()
    opcion = input("Elegí una opción: ").strip()
 
    if opcion == "1":
        agregarProducto()
    elif opcion == "2":
        mostrarProductos()
    elif opcion == "3":
        buscarProductos()
    elif opcion == "4":
        eliminarProducto()
    elif opcion == "5":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Elegí un número del 1 al 5.")