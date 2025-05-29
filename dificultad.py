def dificultad():   # Función para elegir la dificultad del juego
    print('Elige la dificultad:\n 1. Fácil (20 intentos) \n 2. Medio (12 intentos) \n 3. Difícil (5 intentos)')
    import valida
    dificultad = valida.valida(1,3)
    if dificultad == 1:     # guarda el numero de intentos segun la dificultad elegida
        return 20
    elif dificultad == 2:
        return 12
    elif dificultad == 3:
        return 5