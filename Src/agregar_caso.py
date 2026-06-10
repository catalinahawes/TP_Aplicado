import pandas as pd
import os

ARCHIVO = "Datos/informacion_usuarios_argentina_unico.csv"

COLUMNAS = [
    "Nombre y Apellido",
    "Edad",
    "Género",
    "Peso (kg)",
    "Altura (m)",
    "Rasgos Físicos",
    "Zona (Argentina)",
    "Datos Extra"
]


def agregar_caso():
    
    """
    Solicita al usuario los datos de una persona desaparecida y los guarda en el archivo CSV.

    El usuario debe ingresar los siguientes campos:
        - Nombre y Apellido (str): no puede estar vacío.
        - Edad (int): debe ser un número entre 0 y 111.
        - Género (str): debe ser 'Masculino', 'Femenino' u 'Otro'.
        - Peso (float): en kg, entre 1 y 300.
        - Altura (float): en metros, entre 0.5 y 2.5.
        - Rasgos Físicos (str): color de pelo, ojos y tez. No puede estar vacío.
        - Zona (str): provincia o zona de Argentina. No puede estar vacía.
        - Datos Extra (str): información adicional (ropa, tatuajes, etc.). Puede estar vacío.
        
    Cada campo tiene validación. Si el usuario ingresa un valor inválido,
    se le pide que lo vuelva a ingresar hasta que sea correcto.

    Si el archivo CSV no existe, lo crea automáticamente con las columnas correspondientes.
    Si ya existe, carga los datos previos y agrega la nueva fila al final.

    Returns:
        None
    """
    print("\n--- AGREGAR NUEVO CASO ---\n")

    while True:
        nombre = input("Nombre y Apellido: ").strip()
        if nombre:
            break
        print("  ⚠ El nombre no puede estar vacío.")


    while True:
        edad_input = input("Edad: ").strip()
        if edad_input.isdigit() and 0 <= int(edad_input) < 111:
            edad = int(edad_input)
            break
        print("  ⚠ Ingresá una edad válida (número entre 0 y 110).")


    while True:
        genero = input("Género (Masculino / Femenino / Otro): ").strip().capitalize()
        if genero in ["Masculino", "Femenino", "Otro"]:
            break
        print("  ⚠ Ingresá una de las opciones: Masculino, Femenino u Otro.")


    while True:
        try:
            peso = float(input("Peso (kg): ").strip())
            if 1 < peso < 300:
                break
            print("  ⚠ Ingresá un peso válido (entre 1 y 300 kg).")
        except ValueError:
            print("  ⚠ Ingresá un número (por ejemplo: 65.5).")

  
    while True:
        try:
            altura = float(input("Altura (m): ").strip())
            if 0.5 < altura < 2.5:
                break
            print("  ⚠ Ingresá una altura válida (entre 0.5 y 2.5 m).")
        except ValueError:
            print("  ⚠ Ingresá un número (por ejemplo: 1.70).")


    print("Rasgos Físicos (color de pelo, color de ojos, color de tez):")
    while True:
        rasgos = input("  → ").strip()
        if rasgos:
            break
        print("  ⚠ Este campo no puede estar vacío.")


    while True:
        zona = input("Zona (Argentina): ").strip()
        if zona:
            break
        print("Este campo no puede estar vacío.")


    datos_extra = input("Datos Extra (ropa, tatuajes, etc. — podés dejarlo vacío): ").strip()


    nuevo_caso = {
        "Nombre y Apellido": nombre,
        "Edad": edad,
        "Género": genero,
        "Peso (kg)": peso,
        "Altura (m)": altura,
        "Rasgos Físicos": rasgos,
        "Zona (Argentina)": zona,
        "Datos Extra": datos_extra
    }


    if os.path.exists(ARCHIVO):
        df = pd.read_csv(ARCHIVO)
    else:
        df = pd.DataFrame(columns=COLUMNAS)

 
    nueva_fila = pd.DataFrame([nuevo_caso])
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv(ARCHIVO, index=False)

    print(f"\nCaso de '{nombre}' agregado correctamente. ✅\n")
