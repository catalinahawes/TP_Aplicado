# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:36:08 2026

@author: mimib
"""

import pandas as pd
from Src.funcion_validacion import validar_entero_positivo


def modificar_archivo_caso(archivo_activos, archivo_resueltos):
    """
    Busca una denuncia activa por número de caso.

    Si encuentra el caso, lo elimina del archivo de denuncias activas
    y lo agrega al archivo de denuncias resueltas.

    Parameters
    ----------
    archivo_activos : str
        Nombre o ruta del archivo Excel donde están guardados los casos activos.

    archivo_resueltos : str
        Nombre o ruta del archivo CSV donde están guardados los casos resueltos.

    Returns
    -------
    None
        La función no devuelve ningún valor. Modifica los archivos y muestra mensajes por consola.
    """

    try:
        df = pd.read_excel(archivo_activos)

        if len(df) == 0:
            raise ValueError("El archivo de casos activos está vacío.")

        if "N° Caso" not in df.columns:
            raise KeyError("No existe la columna 'N° Caso' en el archivo de casos activos.")

        print("Ingrese el número del caso que desea marcar como resuelto.")

        numero_caso = input("Número de caso: ")
        numero_caso = validar_entero_positivo(numero_caso, "número de caso")

        caso = df[df["N° Caso"] == numero_caso]

        if len(caso) == 0:
            raise ValueError("No se encontró una denuncia con ese número de caso.")

        indice = caso.index[0]
        df_sin_caso = df.drop(indice)

        df_resueltos = pd.read_csv(archivo_resueltos, encoding="latin1")
        df_resueltos = pd.concat([df_resueltos, caso], ignore_index=True)

        df_sin_caso.to_excel(archivo_activos, index=False)
        df_resueltos.to_csv(archivo_resueltos, index=False, encoding="latin1")

        print("El caso fue marcado como resuelto correctamente.")
        print("Se eliminó del archivo de casos activos.")
        print("Se agregó al archivo de casos resueltos.")

    except FileNotFoundError:
        print("Error: no se encontró alguno de los archivos.")

    except ValueError as error:
        print("Error:", error)

    except PermissionError:
        print("Error: no se pudo guardar el archivo.")
        print("Cerrá el archivo si lo tenés abierto.")

    except KeyError as error:
        print("Error:", error)

    except Exception as error:
        print("Ocurrió un error inesperado.")
        print(error)