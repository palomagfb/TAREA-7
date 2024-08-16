class Wallet:
    def __init__(self, nombre_propietario, saldo):
        self.nombre_propietario = nombre_propietario
        self.saldo = saldo

    def agregar_fondos(self, cantidad):
        self.saldo += cantidad

    def deducir_fondos(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        else:
            return False

    def __str__(self):
        return f"😱👛 {self.nombre_propietario}'s saldo en la billetera: {self.saldo}"


class Item:
    def __init__(self, id_item, nombre, precio, cantidad):
        self.id_item = id_item
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio}, Cantidad en stock: {self.cantidad}"


class Tienda:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def listar_items(self):
        print("📜 Lista de Productos")
        print("+------+----------------------+-------+---------+")
        print("|   ID | Nombre del Producto  | Precio| Cantidad|")
        print("+======+======================+=======+=========+")
        for idx, item in enumerate(self.items):
            print(f"|    {idx} | {item.nombre:<20} | {item.precio:>5} | {item.cantidad:>7} |")
        print("+------+----------------------+-------+---------+")

    def verificar_inventario(self, id_item, cantidad):
        if 0 <= id_item < len(self.items):
            item = self.items[id_item]
            if item.cantidad >= cantidad:
                return item
        return None

    def procesar_compra(self, billetera, carrito):
        costo_total = sum(item.precio * item.cantidad for item in carrito)
        if billetera.deducir_fondos(costo_total):
            for item in carrito:
                item.cantidad -= 1
            return True
        else:
            return False


def main():
    # Solicitar nombre y saldo inicial para la billetera del usuario
    nombre_usuario = input("🤖 Por favor, introduce tu nombre: ")
    saldo_inicial = int(input("🏧 Por favor, introduce la cantidad que deseas cargar en tu billetera: "))
    billetera_kei = Wallet(nombre_usuario, saldo_inicial)

    # Inicializar la tienda y agregar productos
    dic_tienda = Tienda()
    dic_tienda.agregar_item(Item(0, "2.5 pulgadas SSD", 13370, 10))
    dic_tienda.agregar_item(Item(1, "3.5 pulgadas HDD", 10980, 10))
    dic_tienda.agregar_item(Item(2, "CPU", 40830, 10))
    dic_tienda.agregar_item(Item(3, "CPU Cooler", 13400, 10))
    dic_tienda.agregar_item(Item(4, "M.2 SSD", 12980, 10))
    dic_tienda.agregar_item(Item(5, "Case de PC", 8727, 10))
    dic_tienda.agregar_item(Item(6, "Tarjeta Gráfica", 23800, 10))
    dic_tienda.agregar_item(Item(7, "Placa Madre", 28980, 10))
    dic_tienda.agregar_item(Item(8, "Memoria RAM", 13880, 10))
    dic_tienda.agregar_item(Item(9, "Unidad de Alimentación", 8980, 10))

    print("🛍️ Comenzando compras...")
    carrito = []
    while True:
        print()
        dic_tienda.listar_items()
        id_item = int(input("⛏ Ingrese el ID del producto que desea comprar: "))
        cantidad = int(input("⛏ Ingrese la cantidad que desea comprar: "))
        item = dic_tienda.verificar_inventario(id_item, cantidad)
        if item:
            carrito.append(Item(item.id_item, item.nombre, item.precio, cantidad))
            print("\n🛒 Contenido del Carrito")
            print("+------+----------------------+-------+---------+")
            print("|   N° | Nombre del Producto  | Precio| Cantidad|")
            print("+======+======================+=======+=========+")
            for idx, item_carrito in enumerate(carrito):
                print(f"|    {idx} | {item_carrito.nombre:<20} | {item_carrito.precio:>5} | {item_carrito.cantidad:>7} |")
            print("+------+----------------------+-------+---------+")
        else:
            print("La cantidad especificada del producto no está disponible en inventario.")

        finalizar_compra = input("\n😭 ¿Desea finalizar la compra? (si/no): ")
        if finalizar_compra.lower() == 'si':
            break

    confirmar_compra = input("💸 ¿Desea confirmar la compra? (si/no): ")
    if confirmar_compra.lower() == 'si':
        if dic_tienda.procesar_compra(billetera_kei, carrito):
            total_pagar = sum(item.precio * item.cantidad for item in carrito)
            print("\n🛒 Contenido del Carrito")
            print("+------+----------------------+-------+---------+")
            print("|   N° | Nombre del Producto  | Precio| Cantidad|")
            print("+======+======================+=======+=========+")
            for idx, item_comprado in enumerate(carrito):
                print(f"|    {idx} | {item_comprado.nombre:<20} | {item_comprado.precio:>5} | {item_comprado.cantidad:>7} |")
            print("+------+----------------------+-------+---------+")
            print(f"🤑 Total a Pagar: {total_pagar}")

            print("\n୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
            print(f"️🛍️ {billetera_kei.nombre_propietario}'s productos adquiridos")
            print("+------+----------------------+-------+---------+")
            print("|   ID | Nombre del Producto  | Precio| Cantidad|")
            print("+======+======================+=======+=========+")
            for idx, item_comprado in enumerate(carrito):
                print(f"|    {idx} | {item_comprado.nombre:<20} | {item_comprado.precio:>5} | {item_comprado.cantidad:>7} |")
            print("+------+----------------------+-------+---------+")
            print(f"{billetera_kei}")
            print("\n📦 Estado del inventario de DIC Store")
            dic_tienda.listar_items()
        else:
            print("La transacción de compra ha fallado. Saldo insuficiente en la billetera.")
    else:
        print("Compra cancelada.")
    print("🎉 ¡Proceso finalizado!")

if __name__ == "__main__":
    main()

