import pandas as pd
import os

from Src.funcion_validacion import (
    validar_nombre_apellido,
    validar_entero_positivo,
    validar_decimal_positivo,
    validar_texto_obligatorio,
)

COLUMNAS = [
    "Nombre y Apellido",
    "Edad",
    "Género",
    "Peso (kg)",
    "Altura (m)",
    "Rasgos Físicos",
    "Zona (Argentina)",
    "Datos Extra",
]


def agregar_caso(archivo_activos):
    """
    Agrega un nuevo caso al archivo de casos activos.

    Parameters
    ----------
    archivo_activos : str
        Nombre o ruta del archivo CSV donde están guardados los casos activos.

    Returns
    -------
    None
        Guarda el nuevo caso en el archivo y muestra mensajes por consola.
    """
    print("AGREGAR NUEVO CASO")

    try:
        nombre = input("Nombre y Apellido: ")
        nombre = validar_nombre_apellido(nombre).strip()
        if nombre.isdigit():
            raise ValueError("El género no puede ser un número. Ingresá un texto (ej: Masculino, Femenino, No Binario).")
        edad = input("Edad: ")
        edad = validar_entero_positivo(edad, "edad")

        genero = input("Género: ")
        genero = validar_texto_obligatorio(genero, "género")
        if genero.isdigit():
            raise ValueError("El género no puede ser un número. Ingresá un texto (ej: Masculino, Femenino, No Binario).")
        peso = input("Peso (kg): ")
        peso = validar_decimal_positivo(peso, "peso")

        altura = input("Altura (m): ")
        altura = validar_decimal_positivo(altura, "altura")

        rasgos = input("Rasgos Físicos: ")
        rasgos = validar_texto_obligatorio(rasgos, "rasgos físicos")

        zona = input("Zona (Argentina): ")
        zona = validar_texto_obligatorio(zona, "zona")

        datos_extra = input("Datos Extra: ")
        datos_extra = validar_texto_obligatorio(datos_extra, "datos extra")
        
        
        if os.path.exists(archivo_activos):
            df = pd.read_excel(archivo_activos, header=0)
            if len(df) > 0:
                proximo_numero = df["N° Caso"].max() + 1
            else:
                proximo_numero = 1
        else:
            df = pd.DataFrame(columns=COLUMNAS)
            proximo_numero = 1

        nueva_fila = {
            "N° Caso": proximo_numero,
            "Nombre y Apellido": nombre,
            "Edad": edad,
            "Género": genero,
            "Peso (kg)": peso,
            "Altura (m)": altura,
            "Rasgos Físicos": rasgos,
            "Zona (Argentina)": zona,
            "Datos Extra": datos_extra,
        }

        if os.path.exists(archivo_activos):
            df = pd.read_excel(archivo_activos, header=0)
        else:
            df = pd.DataFrame(columns=COLUMNAS)

        df.loc[len(df)] = nueva_fila
        df.to_excel(archivo_activos, index=False)

        print("Caso agregado correctamente.")

    except ValueError as error:
        print("Error en los datos ingresados:", error)
        print("No se guardó el caso. Por favor, volvé a intentarlo.")

    except PermissionError:
        print("Error: no se pudo guardar el archivo. Cerralo si está abierto.")
