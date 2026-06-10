import pandas as pd
import os

from funcion_validacion import (
    validar_nombre_apellido,
    validar_entero_positivo,
    validar_decimal_positivo,
    validar_texto_obligatorio,
)

ARCHIVO = "informacion_usuarios_argentina_unico.csv"

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


def agregar_caso():
    print("AGREGAR NUEVO CASO")

    try:
        nombre = validar_nombre_apellido(input("Nombre y Apellido: ").strip())
        edad = validar_entero_positivo(input("Edad: ").strip(), "Edad")
        genero = validar_texto_obligatorio(input("Género: ").strip(), "Género")
        peso = validar_decimal_positivo(input("Peso (kg): ").strip(), "Peso (kg)")
        altura = validar_decimal_positivo(input("Altura (m): ").strip(), "Altura (m)")
        rasgos = validar_texto_obligatorio(input("Rasgos Físicos: ").strip(), "Rasgos Físicos")
        zona = validar_texto_obligatorio(input("Zona (Argentina): ").strip(), "Zona (Argentina)")
        datos_extra = input("Datos Extra (opcional): ").strip()

    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
        print("No se guardó el caso. Por favor, volvé a intentarlo.")
        return

   nueva_fila = [nombre, edad, genero, peso, altura, rasgos, zona, datos_extra]

    if os.path.exists(ARCHIVO):
        df = pd.read_csv(ARCHIVO)
    else:
        df = pd.DataFrame(columns=COLUMNAS)

    #Para agregar fila:
    df.loc[len(df)] = nueva_fila

    df.to_csv(ARCHIVO, index=False)

    print("Caso agregado correctamente.")