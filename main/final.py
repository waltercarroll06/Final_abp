
gastos = []
contador_id = 1


def registrar_gasto():
    global contador_id
    try:
        nombre_gasto = input("ingresa el nombre del gasto: ")
        if nombre_gasto == None or nombre_gasto.strip() == "":
            raise ValueError("Datos no validos, ingrese un nombre para el gasto")
        categoria = input("ingrese la categoria:\nComida | servicio | extra:").lower()
        if categoria not in ["comida", "servicio", "extra"]:
            raise ValueError("datos invalidos, digite solo las opciones porporcionadas")
        valor_gasto = int(input("ingresa el valor de gasto: "))
        if valor_gasto <= 0:
            raise ValueError("Datos incorrectos, numeros mayor a 0")
    except Exception as e:
        print(e)
        return
    gasto = {
    "id": contador_id,
    "nombre": nombre_gasto,
    "categoria": categoria,
    "valor": valor_gasto
    }
    gastos.append(gasto)
    contador_id += 1
    print("Gasto registrado correctamente")

def mostrar_gastos():
    if len(gastos) == 0:
        print("gastos no registrados")
        return
    else:
        for gasto in gastos:
                print(f"{gasto["id"]}. nombre: {gasto["nombre"]} | categoria: {gasto["categoria"]} | valor: {gasto["valor"]}")


def calcular_total():
    total_gastado = 0
    for gasto in gastos:
        total_gastado += gasto["valor"]
    print(f"total gastado: {total_gastado}")
    return total_gastado

def reporte_por_categoria():
    gastos_comida = 0
    gastos_servicio = 0
    gastos_extra = 0
    for gasto in gastos:
        if gasto["categoria"] == "comida":
            gastos_comida += gasto["valor"]
        elif gasto["categoria"] == "servicio":
            gastos_servicio += gasto["valor"]
        elif gasto["categoria"] == "extra":
            gastos_extra += gasto["valor"]
    print(f"Reporte por categoría:")
    print(f"  Comida: {gastos_comida}")
    print(f"  Servicio: {gastos_servicio}")
    print(f"  Extra: {gastos_extra}")

def calcular_saldo(ingreso_hogar, total_gastado):
    ingreso_total = ingreso_hogar - total_gastado
    print(f"Saldo restante: {ingreso_total}")
    if ingreso_total < 0:
        print("⚠️ Alerta: has superado tu presupuesto")


def mostrar_menu():
    print("1. Registrar gasto")
    print("2. Ver lista de gastos")
    print("3. Ver total gastado")
    print("4. Ver saldo restante")
    print("5. Salir")
    
    
def main():
    confirmado = False
    try:
        ingreso_hogar = int(input("ingresa el ingreso total del hogar: "))
        if ingreso_hogar < 0:
            print("Datos no validos, ingrese dato positivo")
        else:
            confirmado = True
            print("Ingreso guardado correctamente")
        while confirmado:
            mostrar_menu()
            try:
                opcion = int(input("Eliga una opcion: "))
            except ValueError:
                print("Opcion invalida, escoga solo un numero valido dentro del menu")
                continue
            if opcion == 1:
                registrar_gasto()
            elif opcion == 2:
                mostrar_gastos()
            elif opcion == 3:
                calcular_total()
                reporte_por_categoria()
            elif opcion == 4:
                total = calcular_total()
                calcular_saldo(ingreso_hogar, total)
                reporte_por_categoria()
            elif opcion == 5:
                print("gracias por utlizar nuestra herramienta")
                break
            else:
                print("Opcion invalida, escoga solo un numero valido dentro del menu")
    except ValueError:
        print("Datos no validos")
        
main()

print("Programa finalizado")