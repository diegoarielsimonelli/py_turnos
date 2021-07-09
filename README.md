# Turnos
##Síntesis
Es un sistema de turnos básico pensado para un consultorio medico en el que trabajen varias especialidades. En este caso, solo atienden dos especialidades: un médico clínico y un psiquiatra. Se desarrollo con conceptos básicos de Python.

##Descripción
El programa inicia en su menú principal.
```
print('¡Bienvenido/a a Turnos para tu Salud!')
    print('Con un N° del 1 al 5 selecciona una opción:')
    print('[1] ¿Desea atenderse con un Médico Clínico?')
    print('[2] ¿Desea atenderse con un psiquiatra?')
    print('[3] ¿Hay mucha demora?')
    print('[4] Listado de pacientes con turno.')
    print('[5] Salir.')
```
Cuando el usuario seleccione la opción 1, el programa le pedirá su nombre y le asignará un turno.  Sucede lo mismo si opta por la opción 2. Cuando selecciona la opción 3 se desplegarán diferentes mensajes de acuerdo a la cantidad de pacientes que tengan los profesionales.

```
if len(fila_psiquiatra) == 0 and len(fila_clinico) == 0:
        print('No hay pacientes en lista de espera. Saque turno, pronto será atendido.')
    elif len(fila_psiquiatra) >= 3 and len(fila_clinico) > 0:
        print('El psiquiatra está atendiendo.Hay mucha demora. Por favor, espere. ')
    elif len(fila_psiquiatra) > 0 and len(fila_clinico) >= 3:
        print('El médico clinico está atendiendo.Hay mucha demora.Por favor, espere.')
    else:
        print(' Los profesionales están atendiendo. Saque turno y espere, por favor.')
```


La opción 4 despliega una lista de todos los pacientes asignados a cada profesional.
La opción 5 es la salida del bucle.

##Crecimiento del Proyecto  

Este programa tiene muchas posibilidades de desarrollo. Se podría personalizar de acuerdo a las necesidades del cliente. En próximas versiones se planea agregarle más funciones como llevar un registro de datos de pacientes, completar la historia clínica, etc.


##Versionado  

Versión 1.0
