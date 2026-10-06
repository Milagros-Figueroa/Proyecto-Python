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
    while true:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("Error: Solo se puede ingresar numeros enteros, sin centavos ni simbolos.")
        elif int(entrada) <= 0:
            print("Error: el precio debe ser mayor a 0.")
        else:
            return int(entrada)

def agregarProducto():
    print("\n--- Agregar producto ---")
    nombre = pedirTexto("Nombre: ")
    categoria = pedirTexto("Categoría: ")
    precio = pedirTexto("Precio (sin centavos): ")

    productos.append([nombre, categoria, precio])
    print(f"Producto '{nombre}' agregado correctamente.")

##def mostrarProductos():
