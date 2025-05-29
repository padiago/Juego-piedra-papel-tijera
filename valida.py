def valida(minimo, maximo): #función para validar que el número introducido sea un número entre el mínimo y el máximo necesario, confirmando que es un numero y no texto
    while True:
        numero_a_validar = input(f'Introduce un número entre {minimo} y {maximo}: ')
        if numero_a_validar == '-100':
            return -100
        elif not numero_a_validar.isdigit():
            print(f'Entrada no válida. Por favor, introduce un número entre {minimo} y {maximo}.')
        else:
            numero_a_validar = int(numero_a_validar)
            if minimo <= numero_a_validar <= maximo:
                return numero_a_validar
            else:
                print(f'Número fuera del rango. Por favor, introduce un número entre {minimo} y {maximo}.')

def v_secreto(minimo, maximo): #realiza la misma función solo que usando el getpass para que no se vea el número introducido
    import getpass
    numero_a_validar = getpass.getpass(f'Introduce un número entre {minimo} y {maximo}: ')
    while True:
        if not numero_a_validar.isdigit():
            numero_a_validar = getpass.getpass(f'Introduce un número entre {minimo} y {maximo}: ')
        else:
            numero_a_validar = int(numero_a_validar)
            if minimo <= numero_a_validar <= maximo:
                return numero_a_validar
            else:
                numero_a_validar = getpass.getpass(f'Introduce un número entre {minimo} y {maximo}: ')