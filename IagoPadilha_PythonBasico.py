# Este programa crea un juego de adivinar el numero
# Zona para importar librerias necesarias, en estos modulos se importarán también pandas, matplotlib, openpyxl, io, getpass y random
import juego
import generador_numeros as gn
import dificultad
import valida
import estadisticas

# Listas necesarias para despues guardar las estadisticas

nombres = []
modos_partida = []
dificultades = []
intentos_realizados_partida = []
resultados = []


opcion = 0
while opcion != 4:      # Bucle para que el programa no se cierre mientras no se elija la opción 4
    print('ADIVINAR EL NÚMERO:\n Se trata de un juego donde adivinar un numero entre 1 y 1.000, se puede jugar tanto en modo solitario como de dos jugadores. \n Elige una opción para comenzar:\n 1. Partida modo solitario \n 2. Partida modo dos jugadores \n 3. Estadisticas \n 4. Salir')
    opcion = valida.valida(1,4)
    if opcion == 1:         # Opción 1: Partida modo solitario
        print('Has elegido la opción 1') 
        intentos = dificultad.dificultad()
        numero_a_adivinar = gn.aleatorio()
        juego.adivinanzas(numero_a_adivinar, intentos, opcion, nombres, modos_partida, dificultades, intentos_realizados_partida, resultados)
    elif opcion == 2:       # Opción 2: Partida modo dos jugadores
        intentos = dificultad.dificultad()
        print('ahora introduce el numero a adivinar')
        numero_a_adivinar = gn.multijugador(1,1000)
        print('ahora toca adivinar el numero')
        juego.adivinanzas(numero_a_adivinar, intentos, opcion, nombres, modos_partida, dificultades, intentos_realizados_partida, resultados)       
    elif opcion == 3:       # Opción 3: Estadisticas
        #Crear un diccionario con los datos de la partida que estaban en listas para poder exportarlos a un excel
        datos_matriz = { 
            'nombre': nombres,
            'modo_partida': modos_partida,
            'dificultad': dificultades, 
            'intentos_realizados': intentos_realizados_partida,
            'resultado': resultados
        }
        estadisticas.estadisticas(numero_a_adivinar, intentos, opcion, nombres, modos_partida, dificultades, intentos_realizados_partida, resultados, datos_matriz) 
    elif opcion == 4:    # Opción 4: Salir (no necesaria pero para mostrar un mensaje final)
        print('Has elegido la opción 4')
        print('Gracias por jugar')