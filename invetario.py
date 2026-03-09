
def separador():
    print("+*30")
def mostrar_opcion():
    opc=int(input("Ingrese la opcion que desea hacer: "))
    print(opc)
def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    
def listar_productos(inventario):
    for producto in inventario:
        print(producto)
    