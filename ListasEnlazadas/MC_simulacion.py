from time import sleep
from threading import Thread
import os

cola = []
valores_significativos = [0]

reparador_ocupado = False
tiempo_reparacion_constante = 5
tiempo_operacional_constante = 10
mc = 0
cl1 = 1
cl2 = 4
cl3 = 9
cl4 = "-"
n = 0


def principal(modo_simulacion):
    global reparador_ocupado, cola, mc, cl1, cl2, cl3, cl4, n
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**SIMULACIÓN DEL PROBLEMA DE INTERFERENCIA DE MÁQUINAS**\n\n")
    if modo_simulacion == 2:
        print("MC: Reloj Maestro\nCL1: Reloj de Evento de Llegada 1\nCL2: Reloj de Evento de Llegada 2\nCL3: Reloj de Evento de Llegada 3\nCL4: Reloj de Evento de Salida 4\nR: Indica si el reparador está ocupado")
        print("-------------")
    while True:
        sleep(0.4 if mc != 0 else 0)
        if mc in obtener_valores_significativos():
            if modo_simulacion == 2:
                print(
                    f"mc: {mc}\t\tcl1: {cl1}\t\tcl2: {cl2}\t\tcl3: {cl3}\t\tcl4: {cl4}\t\tn: {n}\t\tr: {'ocupado' if reparador_ocupado else 'desocupado'}".upper())

        mc += 1  # incrementar el reloj maestro
            
        # Relojes de eventos de llegada iniciales
        if mc == cl1:
            maquina_se_descompone(1, modo_simulacion)
        elif mc == cl2:
            maquina_se_descompone(2, modo_simulacion)
        elif mc == cl3:
            maquina_se_descompone(3, modo_simulacion)


def maquina_se_descompone(id_maquina, modo_simulacion):
    global reparador_ocupado, cola, mc, cl1, cl2, cl3, cl4, n

    print(f"Una máquina se descompone en el tiempo {mc}\n" if modo_simulacion == 1 else "", end="")
    # Incrementar n
    n += 1
    print(f"n = n + 1\n" if modo_simulacion == 1 else "", end="")

    if mc == cl1:
        cl1 = "-"
    elif mc == cl2:
        cl2 = "-"
    elif mc == cl3:
        cl3 = "-"

    print(f"(?) ¿El reparador está ocupado?\n" if modo_simulacion == 1 else "", end="")
    if reparador_ocupado:
        cola.append(id_maquina)
        print(
            f"SÍ. El reparador está ocupado, únase a la cola\n" if modo_simulacion == 1 else "", end="")
    else:
        print(f"NO. El reparador está DESOCUPADO\n" if modo_simulacion == 1 else "", end="")
        reparador_ocupado = True
        print(
            f"El reparador se vuelve ocupado\n" if modo_simulacion == 1 else "", end="")
        cl4 = mc + tiempo_reparacion_constante
        Thread(target=iniciar_reparacion, args=(id_maquina, modo_simulacion,)).start()


def iniciar_reparacion(id_maquina, modo_simulacion):
    global reparador_ocupado, cola, mc, cl1, cl2, cl3, cl4, n
    print(f"Comienza la reparación\n" if modo_simulacion == 1 else "", end="")

    while True:
        sleep(0.01)
        if cl4 == mc:
            reparacion_completa(id_maquina, modo_simulacion)
            break


def reparacion_completa(id_maquina, modo_simulacion):
    global reparador_ocupado, cola, mc, cl1, cl2, cl3, cl4, n
    print(f"Una máquina se ha reparado en el tiempo {mc}\n" if modo_simulacion == 1 else "", end="")
    n -= 1
    print(f"n = n - 1\n" if modo_simulacion == 1 else "", end="")

    if id_maquina == 1:
        cl1 = mc + tiempo_operacional_constante
    elif id_maquina == 2:
        cl2 = mc + tiempo_operacional_constante
    elif id_maquina == 3:
        cl3 = mc + tiempo_operacional_constante

    print(f"(?) ¿Otra máquina espera en la cola?\n" if modo_simulacion == 1 else "", end="")
    if n > 0:  # Si otra máquina espera en la cola
        print(f"SÍ. Otra máquina espera en la cola\n" if modo_simulacion == 1 else "", end="")
        cl4 = mc + tiempo_reparacion_constante
        Thread(target=iniciar_reparacion, args=(cola.pop(0), modo_simulacion,)).start()
    else:  # La cola está vacía
        reparador_ocupado = False
        print(f"NO. La cola está vacía\n" if modo_simulacion == 1 else "", end="")
        print(f"El reparador está ahora DESOCUPADO\n" if modo_simulacion == 1 else "", end="")


def obtener_valores_significativos():
    lista_CL = []
    if cl1 != "-":
        lista_CL.append(cl1)
    if cl2 != "-":
        lista_CL.append(cl2)
    if cl3 != "-":
        lista_CL.append(cl3)
    if cl4 != "-":
        lista_CL.append(cl4)

    valores_significativos.append(min(lista_CL))
    return valores_significativos




if __name__ == "__main__":

    print("**SIMULACIÓN DEL PROBLEMA DE INTERFERENCIA DE MÁQUINAS**\n")
    principal(2)
