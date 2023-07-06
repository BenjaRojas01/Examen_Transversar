from Cliente import *
def llenar(lista):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if len(str(x)) < 2:
                lista[f][c] = '0' + str(x)
            else:
                lista[f][c] = str(x)
def mostrar(lista):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' | ' + lista[f][c] + ' | '
        print(fila)

def comprar(lista, num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if x == num_asiento:
                lista[f][c] = 'xx'

def validarAsiento(lista, num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if x == num_asiento:
                if lista[f][c] == 'xx':
                    return False
        return True

def comprarEntrada(lista, lista_asistentes):
    try:
        cantidad = int(input("Ingrese el numero de entradas: (1-3): "))
        if cantidad >=1 and cantidad <=3:
            compra = 0
            while compra < cantidad:
                mostrar(lista)
                num_asiento = int(input("Ingrese el numero de Asiento: "))
                if num_asiento >= 1 and num_asiento <= 100:
                    disp = validarAsiento(lista, num_asiento)
                    if disp == True:
                        comprar(lista, num_asiento)
                        agregarAsistente(lista_asistentes, num_asiento)
                        compra = compra + 1
                    else:
                        print("Asiento no se encuentra disponible")
                else:
                    print("El numero del asiento debe estar entre (1-100)")
        else:
            print("El numero de Entradas debe ser entre 1-3")

    except:
        print("Ingrese solo Digitos")

def agregarAsistente(lista_asistentes, num_asiento):
    a = Cliente()
    c = False
    while c == False:
        c = a.setRut(input("Ingrese su Rut (7-8 Digitos): "))
    a.Nombre = input("Ingrese su Nombre: ")
    a.Apellido = input("Ingrese su Apellido: ")
    a.Num_asiento = num_asiento
    if num_asiento >=1 and num_asiento <=20:
        a.Valor = 120000
    if num_asiento >=21 and num_asiento <=50:
        a.Valor = 80000
    if num_asiento >=51 and num_asiento <=100:
        a.Valor = 50000
    print("Se Agrego Asistente")
    lista_asistentes.append(a)

def listadoAsistentes(lista_asistentes):
    for asistentes in lista_asistentes:
        print("----------------------------------------------------------------------------")
        print(f"Asistente: Rut: {asistentes.Rut} Nombre: {asistentes.Nombre} {asistentes.Apellido}  / Numero de Asiento: {asistentes.Num_asiento}")
        print("----------------------------------------------------------------------------")

def totales(lista_asistentes):
    p = 0
    g = 0
    s = 0
    tot_p = 0
    tot_g = 0
    tot_s = 0

    for valor in lista_asistentes:
        if valor.Valor == 120000:
            p += 1
            tot_p =tot_p + 120000
        if valor.Valor == 80000:
            g += 1
            tot_g += 80000
        if valor.Valor == 50000:
            s += 1
            tot_s += 50000

    t_e = p + g + s
    tot_ganancias = tot_p + tot_g + tot_s
    print(f"Entradas Platinum: \t{p} Ganancias Entradas Platinum: \t{tot_p}")
    print(f"Entradas Gold:     \t{g} Ganancias Entradas Gold:     \t{tot_g}")
    print(f"Entradas Silver:   \t{s} Ganancias Entradas Silver:   \t{tot_s}")
    print(f"Total Entradas :   \t{t_e}  /  Total Ganancias:       \t{tot_ganancias}")

def salir():
    print("Cerrando Sesion")
    print("Benjamin Rojas (06/07/2023)")
    return False
