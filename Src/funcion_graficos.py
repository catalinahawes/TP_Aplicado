import matplotlib.pyplot as plt

def grafico_barras_zona(df):
    """Gráfico de barras por zona (como en la clase)"""
    
    zonas = df['Zona (Argentina)'].tolist()
    
    zonas_unicas = []
    cantidades = []
    
    for zona in zonas:
        if zona not in zonas_unicas:
            zonas_unicas.append(zona)
            cantidades.append(zonas.count(zona))
    
    plt.figure()
    plt.bar(x=zonas_unicas, height=cantidades, color="blue")
    plt.title("Casos por zona")
    plt.xlabel("Zona")
    plt.ylabel("Cantidad de casos")
    plt.show()



def grafico_torta_genero(df):
    """Gráfico de torta por género"""
    
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
    """Histograma simple de edades"""
    
    edades = df['Edad'].tolist()
    
    plt.figure()
    plt.hist(edades, color="green")
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Cantidad de casos")
    plt.show()



def menu_graficos(df):
    while True:
        print("Seleccione el grafico que desee ver:")
        print("1. Barras por zona")
        print("2. Torta por género")
        print("3. Histograma de edades")
        print("4. Ver los 3 gráficos")
        print("5. Salir")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            grafico_barras_zona(df)
        elif opcion == "2":
            grafico_torta_genero(df)
        elif opcion == "3":
            grafico_histograma_edad(df)
        elif opcion == "4":
            grafico_barras_zona(df)
            grafico_torta_genero(df)
            grafico_histograma_edad(df)
        elif opcion == "5":
            print("Saliendo del menú de gráficos...")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")