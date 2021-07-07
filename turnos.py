

fila_clinico = {}
fila_psiquiatra = {}

def _menu():
    print('¡Bienvenido/a a Turnos para tu Salud!')
    print('Con un N° del 1 al 5 selecciona una opción:')
    print('[1] ¿Desea atenderse con un Médico Clinico?')
    print('[2] ¿Desea atenderse con un psiquiatra?')
    print('[3] ¿Hay mucha demora?')
    print('[4] Listado de pacientes con turno.')
    print('[5] Salir.')

def xnombre_paciente():
    nombre_paciente = None

    while not nombre_paciente:
        nombre_paciente = input('¿Cuál es el nombre del paciente? \n')

    return nombre_paciente

def _ya_tiene_turno(nombre_paciente):
    print('El paciente', nombre_paciente, 'ya tiene un turno asignado. Por favor, espere a ser atendido.')


def agregar_paciente(tipo_turno, nombre_paciente):
    global fila_psiquiatra
    global fila_clinico
    n = False
    if len(fila_psiquiatra) > 0 and len(fila_clinico) > 0:  
        for val1 in fila_clinico.values():
            if val1 == nombre_paciente:
                n = True
            else:
                n = False
        for val2 in fila_psiquiatra.values():
            if val2 == nombre_paciente:
                n = True
            else:
                n = False

    if n == False:
        if tipo_turno == 1:
            l1 = len(fila_clinico) + 1
            t1 = 'C-' + str(l1)
            fila_clinico[t1] = nombre_paciente
            print('El paciente',nombre_paciente,' tiene el turno  ' + t1)
        elif tipo_turno == 2:
            l2 = len(fila_psiquiatra) + 1
            t2 = 'P-' + str(l2)
            fila_psiquiatra[t2] = nombre_paciente
            print('El paciente',nombre_paciente,' tiene el turno  ' + t2)
    else:
        _ya_tiene_turno(nombre_paciente)

def atender_paciente():
    global fila_psiquiatra
    global fila_clinico
    if len(fila_psiquiatra) == 0 and len(fila_clinico) == 0:
        print('No hay pacientes en lista de espera. Saque turno, pronto será atendido.')
    elif len(fila_psiquiatra) >= 3 and len(fila_clinico) > 0:
        print('El psiquiatra está atendiendo.Hay mucha demora. Por favor, espere. ')
    elif len(fila_psiquiatra) > 0 and len(fila_clinico) >= 3:
        print('El médico clinico está atendiendo.Hay mucha demora.Por favor, espere.')
    else:
        print(' Los profesionales están atendiendo. Saque turno y espere, por favor.')

def listar_paciente():
    global fila_psiquiatra
    global fila_clinico

    print('Pacientes para el Médico Clinico:')
    for key, value in fila_clinico.items():
        print('Turno:',key,'Nombre:',value)

    print('Pacientes para el Psiquiatra:')
    for key, value in fila_psiquiatra.items():
        print('Turno:',key,'Nombre:',value)


if __name__ == '__main__':
    salir = False
    while not salir:
        _menu()
        num = int(input())

        if num == 1:
            nombre_paciente = xnombre_paciente()
            agregar_paciente(1, nombre_paciente)
        elif num == 2:
            nombre_paciente = xnombre_paciente()
            agregar_paciente(2, nombre_paciente)
        elif num == 3:
            atender_paciente()
        elif num == 4:
            listar_paciente()
        elif num == 5:
            salir = True
            print('Gracias por venir, vuelva pronto.')
        else:
            print('¡Error! Ingrese un N° del 1 al 5')
