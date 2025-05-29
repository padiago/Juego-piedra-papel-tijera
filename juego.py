def adivinanzas(numero_a_adivinar, intentos, opcion, nombres, modos_partida, dificultades, intentos_realizados_partida, resultados):
    import valida 
    intentos_realizados = 0
    ganador = False # Variable para saber si se ha acertado el número y poder guardar los datos
    while intentos_realizados < intentos and ganador == False: #bucle del juego en si mismo
        numero_intento = valida.valida(1,1000)  # Validar que el número introducido sea un número entre 1 y 1000
        intentos_realizados = intentos_realizados + 1
        if intentos_realizados < intentos:
            if numero_intento ==  -100:
                print(numero_a_adivinar)
            elif numero_intento > numero_a_adivinar:
                restante = intentos - intentos_realizados
                print('el numero buscado es menor, te quedan:', restante, 'intentos')
            elif numero_intento < numero_a_adivinar:
                restantes = intentos - intentos_realizados
                print('el numero buscado es mayor, te quedan', restantes, 'intentos')
            elif numero_intento == numero_a_adivinar:
                print('Has acertado. Tuviste un total de', intentos_realizados, 'intentos')
                ganador = True
        else:
            print('has perdido')
    
    #Parte donde guardar los datos para cuando se desee sacar las estadisticas, tanto mensaje personalizado como más datos para tener completo el excel de estadisticas
    nombre = input('Introduce tu nombre para guardar los datos: ') # No pongo un bucle para confirmar que el nombre es correcto porque se acepta cualquier texto por nombre (Iago, I4GO, 1234, etc)
    print(F'Muchas gracias por jugar {nombre}')
    if ganador == True:
        if intentos == 5:
            print('aun encima ganaste en dificultad dificil! eres un crack. Esperamos verte por aquí pronto')
        else:
            print('Después de ganar, esperamos verte por aquí pronto para ver si sigues teniendo esa suerte!')
    else:
        if opcion == 5:
            print('En ese nivel dificultad estaba complicado, pero no te rindas, esperamos que sigas dandole hasta que lo consigas')
        else:
            print('No te preocupes, seguro que la próxima vez lo consigues. Esperamos verte por aquí pronto')
    
    if opcion == 1:
        opcion = 'Solitario'
    else:
        opcion = 'Dos jugadores'
    if intentos == 20:
        dificultad = 'Fácil'
    elif intentos == 12:
        dificultad = 'Medio'
    else:
        dificultad = 'Difícil'
    if ganador == True:
        resultado = 'Ganador'
    else:
        resultado = 'Perdedor'

    #Agregar los datos a las listas
    nombres.append(nombre)
    modos_partida.append(opcion)
    dificultades.append(dificultad)
    intentos_realizados_partida.append(intentos_realizados)
    resultados.append(resultado)