import pandas as pd

ARCHIVO = "Datos/informacion_usuarios_argentina_unico.csv"
from Src.funcion_validacion import validar_nombre_apellido


def filtrar_participante(df, nombre_buscado):
    """
    Filtra el DataFrame y devuelve las filas que coinciden con el nombre buscado.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los casos activos.
    nombre_buscado : str
        Nombre y apellido del participante a buscar.

    Returns
    -------
    pandas.DataFrame
        DataFrame con las coincidencias encontradas (puede estar vacío).
    """
    if not nombre_buscado:
        return pd.DataFrame()

    coincidencias = df[df['Nombre y Apellido'] == nombre_buscado.strip()]
    return coincidencias

def mostrar_caso_especifico(df):
    """
    Solicita un nombre al usuario y muestra la información detallada del caso encontrado.
    Si no encuentra el caso, pregunta si desea reintentar la búsqueda.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los casos activos.

    Returns
    -------
    None
    """
    while True:
        nombre_buscado = input("\nIngrese nombre y apellido: ").strip()
        nombre_buscado = validar_nombre_apellido(nombre_buscado)

        resultado = filtrar_participante(df, nombre_buscado)

        if len(resultado) > 0:
            print("Caso encontrado...")
            caso = resultado.iloc[0]
            for columna, valor in caso.items():
                print(f"{columna:22} : {valor}")
            return  

        else:
            print("No se encontraron registros con ese nombre.")

            
            while True:
                reintentar = input("\n¿Desea reintentar la búsqueda? (si/no): ").strip().lower()
                if reintentar in ['si', 's', 'yes', 'y']:
                    break 
                elif reintentar in ['no', 'n']:
                    print("Volviendo al menú principal...")
                    return  
                else:
                    print("Por favor, responda 'si' o 'no'.")




