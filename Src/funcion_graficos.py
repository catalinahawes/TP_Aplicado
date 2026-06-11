import matplotlib.pyplot as plt
from Src.funcion_validacion import validar_entero_positivo
def grafico_barras_zona(df):
    '''
    Genera un gráfico de barras con la cantidad de casos por zona.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene los datos de los casos, 
        debe incluir la columna 'Zona (Argentina)'.

    Returns
    -------
    None
        Muestra el gráfico en pantalla.
    '''
    
    zonas = df['Zona (Argentina)'].tolist()
    
    zonas_unicas = []
    cantidades = []
    
    for zona in zonas:
        if zona not in zonas_unicas:
            zonas_unicas.append(zona)
            cantidades.append(zonas.count(zona))
    
    plt.figure()
    plt.bar(x=zonas_unicas, height=cantidades)
    plt.title("Casos por zona")
    plt.xlabel("Zona")
    plt.ylabel("Cantidad de casos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def grafico_torta_genero(df):
    '''
    Genera un gráfico de torta con el porcentaje de casos por género.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene los datos de los casos, 
        debe incluir la columna 'Género'.

    Returns
    -------
    None
        Muestra el gráfico en pantalla.
    '''
    
    generos = df['Género'].tolist()
    
    generos_unicos = []
    cantidades = []
    
    for genero in generos:
        if genero not in generos_unicos:
            generos_unicos.append(genero)
            cantidades.append(generos.count(genero))
    
    plt.figure()
    plt.pie(cantidades, labels=generos_unicos)
    plt.title("Casos por género")
    plt.show()




def grafico_histograma_edad(df):
    '''
    Genera un histograma con la distribución de edades de los casos.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene los datos de los casos, 
        debe incluir la columna 'Edad'.

    Returns
    -------
    None
        Muestra el gráfico en pantalla.
    '''
    
    edades = df['Edad'].tolist()
    
    plt.figure()
    plt.hist(edades)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Cantidad de casos")
    plt.show()

def menu_graficos(df):
    '''
    Muestra un menú interactivo para seleccionar y visualizar gráficos.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos de los casos. (genero,edad,zonas,etc)

    Returns
    -------
    None
        Ejecuta los gráficos según la opción elegida por el usuario.
    '''
    while True:
        print("Seleccione el grafico que desee ver:")
        print("1. Barras por zona")
        print("2. Torta por género")
        print("3. Histograma de edades")
        print("4. Ver los 3 gráficos")
        print("5. Salir")
        
        try:
            opcion_str = input("Elegí una opción: ")
            opcion = validar_entero_positivo(opcion_str, "opción del menú")

            if opcion == 1:
                grafico_barras_zona(df)
            elif opcion == 2:
                grafico_torta_genero(df)
            elif opcion == 3:
                grafico_histograma_edad(df)
            elif opcion == 4:
                print("Mostrando los 3 gráficos...")
                grafico_barras_zona(df)
                grafico_torta_genero(df)
                grafico_histograma_edad(df)
            elif opcion == 5:
                print("Saliendo del menú de gráficos...")
                break
            else:
                print("Opción inválida. Elegí un número entre 1 y 5.")

        except ValueError as error:
            print("Error de validación:", error)
            print("Por favor, intentá de nuevo con un número del 1 al 5.")
