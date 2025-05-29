def estadisticas(numero_a_adivinar, intentos, opcion, nombres, modos_partida, dificultades, intentos_realizados_partida, resultados, datos_matriz):
    import pandas as pd
    import matplotlib.pyplot as plt
    from openpyxl import load_workbook
    from openpyxl.drawing.image import Image
    import io
    import valida
    
    ruta = 'C:\EjerciciosPython\estadisticas.xlsx'

    # transforma el diccionario antes creado en un DataFrame para poder ser exportado a un archivo Excel
    datos_matriz = pd.DataFrame(datos_matriz)
    datos_matriz = datos_matriz.set_index('nombre')
    print('Opciones para extraer las estadisticas:\n 1. Filtrado por nombre\n 2. Filtrado por los 10 mejores\n 3. Filtrado por los 10 peores\n 4. Mostrar todos los datos')
    filtrar_df = valida.valida(1,4)

    # Aqui se filtran los datos segun la opción elegida
    if filtrar_df == 1:
        nombre_filtrar = input('Introduce el nombre a filtrar: ')
        while nombre_filtrar not in datos_matriz['nombre']:
            print('Nombre no encontrado')
            nombre_filtrar = input('Introduce el nombre a filtrar: ')
        else:
            datos_matriz = datos_matriz[datos_matriz['nombre'] == nombre_filtrar]
        print(F'Datos filtrados por {nombre_filtrar}')
    elif filtrar_df == 2:
        datos_matriz = datos_matriz.sort_values('intentos_realizados')
        datos_matriz = datos_matriz.head(10)
        print('Datos de los 10 mejores')
    elif filtrar_df == 3:
        datos_matriz = datos_matriz.sort_values('intentos_realizados')
        datos_matriz = datos_matriz.tail(10) 
        print('Datos de los 10 peores')
    else:
        print('Total de estadisticas')

    # Guardar los datos en un archivo Excel
    datos_matriz.to_excel(ruta)

    # Crear el gráfico con matplotlib
    plt.figure(figsize=(8, 5))  # Tamaño de la figura
    plt.bar(datos_matriz['nombre'], datos_matriz['intentos_realizados'], color='skyblue')
    plt.xlabel('Nombre')
    plt.ylabel('Intentos Realizados')
    plt.title('Estadísticas de Intentos Realizados')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Guardar el gráfico
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    # Abrir el archivo Excel existente 
    wb = load_workbook(ruta)
    ws = wb.active

    # Insertar el gráfico en la hoja de cálculo
    img = Image(img_data)
    ws.add_image(img, 'E2')

    # Guardar el archivo Excel
    wb.save(ruta)

    print('Datos y gráfico guardados en ', ruta)
