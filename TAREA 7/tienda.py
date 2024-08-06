import datetime
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.wallet = 0  
        self.carrito = CarritoCompra()

    def cargar_saldo(self, cantidad):
        self.wallet += cantidad

    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}:")
        self.carrito.mostrar_contenido()

    def confirmar_compra(self):
        print("¿Desea confirmar la compra?")
        confirmacion = input("yes/no: ").strip().lower()
        if confirmacion == "yes":
            self.carrito.finalizar_compra()
        else:
            print("Compra cancelada.")

    def mostrar_resumen(self, tienda):
        print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
        print(f"️ ️{self.nombre}の所有物")
        self.carrito.mostrar_contenido()
        print(f"Saldo en la billetera de {self.nombre}: {self.wallet}")
        print("Inventario de la tienda")
        tienda.mostrar_inventario()
        print(f"Saldo en la billetera de la tienda: {tienda.wallet}")
        print("Contenido del carrito")
        self.carrito.mostrar_contenido()
        print("Total a pagar:", self.carrito.total)
        print("Fin")
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.wallet = 0  
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print(f"+------+-----------+-------+------+")
        print(f"| Número | Nombre        | Precio | Cantidad |")
        print(f"+======+===========+=======+======+")
        for i, producto in enumerate(self.inventario):
            print(f"| {i}    | {producto.nombre} | {producto.precio} | {producto.cantidad} |")
        print(f"+------+-----------+-------+------+")

    def vender_producto(self, numero_producto, cantidad):
        producto = self.inventario[numero_producto]
        if producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
            return Producto(producto.nombre, producto.precio, cantidad)
        else:
            print("No hay suficiente stock disponible.")
            return None

    def recibir_pago(self, total):
        self.wallet += total
class CarritoCompra:
    def __init__(self):
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        self.items.append(Producto(producto.nombre, producto.precio, cantidad))
        self.total += producto.precio * cantidad

    def mostrar_contenido(self):
        if not self.items:
            print("El carrito está vacío.")
        else:
            print(f"+------+-----------+-------+------+")
            print(f"| Número | Nombre        | Precio | Cantidad |")
            print(f"+======+===========+=======+======+")
            for i, item in enumerate(self.items):
                print(f"| {i}    | {item.nombre} | {item.precio} | {item.cantidad} |")
            print(f"+------+-----------+-------+------+")

    def finalizar_compra(self):
        print("Compra confirmada.")
        self.items = []
        self.total = 0
usuario = Usuario("kei kamiguchi")
usuario.cargar_saldo(1000000)

tienda = Tienda("DICストア")
tienda.agregar_producto(Producto("SSD de 2.5 pulgadas", 13370, 10))
tienda.agregar_producto(Producto("HDD de 3.5 pulgadas  ", 10980, 10))
tienda.agregar_producto(Producto("CPU (Procesador) ", 40830, 10))
tienda.agregar_producto(Producto("Refrigeración para CPU (CPU Cooler)", 13400, 10))
tienda.agregar_producto(Producto("SSD M.2", 12980, 10))
tienda.agregar_producto(Producto("Caja de PC (PC Case) ", 8727, 10))
tienda.agregar_producto(Producto("Tarjeta gráfica (Graphics Card) ", 23800, 10))
tienda.agregar_producto(Producto("Placa base (Motherboard)", 28980, 10))
tienda.agregar_producto(Producto(" Memoria RAM (Memory) ", 13880, 10))
tienda.agregar_producto(Producto("Unidad de alimentación (Power Supply Unit) ", 8980, 10))
print("Comenzando las compras")
while True:
    print(" Lista de productos")
    tienda.mostrar_inventario()
    
    print("️️Ingrese el número del producto")
    numero_producto = int(input().strip())

    print("Ingrese la cantidad del producto")
    cantidad = int(input().strip())

    producto_comprado = tienda.vender_producto(numero_producto, cantidad)

    if producto_comprado:
        usuario.carrito.agregar_item(producto_comprado, cantidad)
        print("🛒 Contenido del carrito")
        usuario.mostrar_carrito()
    else:
        print("Seleccione nuevamente")

    print(" Total a pagar:", usuario.carrito.total)
    print(" ¿Desea finalizar las compras? (yes/no)")
    terminar_compra = input().strip().lower()

    if terminar_compra == "yes":
        usuario.confirmar_compra()
        tienda.recibir_pago(usuario.carrito.total)
        usuario.wallet -= usuario.carrito.total
        break
usuario.mostrar_resumen(tienda)
