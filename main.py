import numpy as np
from Funciones import *

lista = np.full((10, 10), '---')
llenar(lista)
lista_asistentes = []
ciclo = True
while ciclo:
    print("-------------------------")
    print("Bienvenido a Creativos.cl")
    print("Concierto Vip Michael Jam")
    print("-------------------------")
    print("1) Comprar Entradas")
    print("2) Mostrar Ubicaciones Disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")

    try:
        op = int(input("Ingrese una opcion (1-5): "))
        match op:
            case 1:
                comprarEntrada(lista, lista_asistentes)
            case 2:
                mostrar(lista)
            case 3:
                listadoAsistentes(lista_asistentes)
            case 4:
                totales(lista_asistentes)

            case 5:
                ciclo = salir()

    except:
        print("Ingrese solo Digitos")