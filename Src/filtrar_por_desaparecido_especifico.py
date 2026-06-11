import pandas as pd

ARCHIVO = "Datos/informacion_usuarios_argentina_unico.csv"
from funcion_validacion import validar_nombre_apellido


def filtrar_participante(df, nombre_buscado):
    """
    Descripción: filtra el DataFrame según el nombre del participante.
    Parámetros: 
        df (DataFrame) tabla con los datos
        nombre_buscado (str) nombre y apellido del participante
    Retorno: DataFrame filas que coinciden o DataFrame vacío si no hay coincidencias
    """
    
    if not nombre_buscado:
        return pd.DataFrame()
    
    coincidencias = df[df['Nombre y Apellido'] == nombre_buscado]
    
    return coincidencias


def mostrar_caso_especifico(df):
    """
    Descripción: solicita un nombre al usuario y muestra la información especifica de ese participante.
    Parámetros: df (DataFrame)
    Retorno: None
    """
    
    nombre_buscado = input("Ingrese nombre y apellido: ").strip()
    nombre_buscado = validar_nombre_apellido(nombre_buscado)
   
    resultado = filtrar_participante(df, nombre_buscado)
   
    if len(resultado) > 0:
       print("Caso encontrado:")
       print(resultado.to_string(index=False))
    else:
       print("No se encontraron registros")
   
    return nombre_buscado




