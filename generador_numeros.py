def aleatorio(): #para poder generar un numero aleatorio para la partida solitaria
    import random
    return random.randint(1, 1000)

def multijugador(minimo, maximo): #para poder introducir el numero a adivinar en la partida de dos jugadores
    import valida
    return valida.v_secreto(minimo, maximo)