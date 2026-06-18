# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:12:57 2026

@author: mimib
"""
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Funciones del proyecto
from Src.funcion_validacion import (
    validar_nombre_apellido,
    validar_entero_positivo,
    validar_decimal_positivo,
    validar_texto_obligatorio,
)

from Src.filtrar_por_desaparecido_especifico import filtrar_participante
from Src.funcion_graficos import (
    grafico_barras_zona,
    grafico_torta_genero,
    grafico_histograma_edad,
)


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Dashboard de Casos",
    page_icon="📋",
    layout="wide"
)

RUTA_DATOS = "Datos"
ARCHIVO_ACTIVOS = os.path.join(RUTA_DATOS, "informacion_usuarios.xlsx")
ARCHIVO_RESUELTOS = os.path.join(RUTA_DATOS, "Casos resueltos.xlsx")

COLUMNAS = [
    "N° Caso",
    "Nombre y Apellido",
    "Edad",
    "Género",
    "Peso (kg)",
    "Altura (m)",
    "Rasgos Físicos",
    "Zona (Argentina)",
    "Datos Extra",
]


# ============================================================
# FUNCIONES AUXILIARES PARA STREAMLIT
# ============================================================

def cargar_excel(ruta_archivo):
    """
    Carga un archivo Excel.
    Si el archivo no existe, devuelve un DataFrame vacío con las columnas esperadas.
    """
    if os.path.exists(ruta_archivo):
        return pd.read_excel(ruta_archivo, header=0)
    else:
        return pd.DataFrame(columns=COLUMNAS)


def guardar_excel(df, ruta_archivo):
    """
    Guarda un DataFrame en un archivo Excel.
    """
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    df.to_excel(ruta_archivo, index=False)


def validar_estructura(df):
    """
    Valida que el archivo tenga las columnas mínimas necesarias.
    """
    if df.empty:
        return

    columnas_faltantes = []

    for columna in COLUMNAS:
        if columna not in df.columns:
            columnas_faltantes.append(columna)

    if len(columnas_faltantes) > 0:
        raise ValueError(
            "Faltan columnas obligatorias en el archivo: "
            + ", ".join(columnas_faltantes)
        )


def obtener_proximo_numero_caso(df):
    """
    Calcula el próximo número de caso.
    """
    if df.empty or "N° Caso" not in df.columns:
        return 1

    numeros = pd.to_numeric(df["N° Caso"], errors="coerce")

    if numeros.dropna().empty:
        return 1

    return int(numeros.max()) + 1


def mostrar_grafico_streamlit(funcion_grafico, df):
    """
    Ejecuta una función de gráficos del proyecto y la muestra en Streamlit.

    Las funciones originales usan plt.show(), no return fig.
    Por eso capturamos la figura actual con matplotlib.
    """
    plt.close("all")

    funcion_grafico(df)

    figuras = plt.get_fignums()

    if len(figuras) == 0:
        st.warning("No se pudo generar el gráfico.")
        return

    fig = plt.figure(figuras[-1])
    st.pyplot(fig)
    plt.close("all")


def mostrar_mensaje_guardado():
    """
    Muestra mensajes guardados después de un st.rerun().
    """
    if "mensaje_exito" in st.session_state:
        st.success(st.session_state["mensaje_exito"])
        del st.session_state["mensaje_exito"]

    if "mensaje_error" in st.session_state:
        st.error(st.session_state["mensaje_error"])
        del st.session_state["mensaje_error"]


# ============================================================
# CARGA DE DATOS
# ============================================================

try:
    df_activos = cargar_excel(ARCHIVO_ACTIVOS)
    df_resueltos = cargar_excel(ARCHIVO_RESUELTOS)

    validar_estructura(df_activos)

except ValueError as e:
    st.error(str(e))
    st.stop()

except PermissionError:
    st.error("No se pudo abrir o guardar el archivo. Cerrá el Excel si está abierto.")
    st.stop()

except Exception as e:
    st.error(f"Ocurrió un error inesperado al cargar los datos: {e}")
    st.stop()


# ============================================================
# INTERFAZ PRINCIPAL
# ============================================================

st.title("Dashboard de Casos")
st.write("Sistema de gestión y análisis de denuncias")

mostrar_mensaje_guardado()

st.info(
    f"""
    **Archivo de casos activos:** `{ARCHIVO_ACTIVOS}`  
    **Archivo de casos resueltos:** `{ARCHIVO_RESUELTOS}`
    """
)

if st.button("Actualizar datos"):
    st.rerun()


# ============================================================
# MENÚ LATERAL
# ============================================================

opcion = st.sidebar.radio(
    "Menú principal",
    [
        "Inicio",
        "Casos activos",
        "Buscar caso específico",
        "Agregar nuevo caso",
        "Estadísticas y gráficos",
        "Marcar caso como resuelto",
        "Casos resueltos",
    ]
)


# ============================================================
# INICIO
# ============================================================

if opcion == "Inicio":
    st.subheader("Resumen general")

    total_activos = len(df_activos)
    total_resueltos = len(df_resueltos)
    total_general = total_activos + total_resueltos

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Casos activos", total_activos)

    with col2:
        st.metric("Casos resueltos", total_resueltos)

    with col3:
        st.metric("Total de casos", total_general)

    st.divider()

    col4, col5 = st.columns(2)

    with col4:
        if not df_activos.empty and "Edad" in df_activos.columns:
            edades = pd.to_numeric(df_activos["Edad"], errors="coerce")
            promedio_edad = edades.mean()

            if pd.notna(promedio_edad):
                st.metric("Edad promedio", round(promedio_edad, 1))
            else:
                st.metric("Edad promedio", "Sin datos")
        else:
            st.metric("Edad promedio", "Sin datos")

    with col5:
        if not df_activos.empty and "Zona (Argentina)" in df_activos.columns:
            zona_mas_frecuente = df_activos["Zona (Argentina)"].mode()

            if not zona_mas_frecuente.empty:
                st.metric("Zona con más casos", zona_mas_frecuente.iloc[0])
            else:
                st.metric("Zona con más casos", "Sin datos")
        else:
            st.metric("Zona con más casos", "Sin datos")

    st.divider()

    st.subheader("Vista rápida de casos activos")

    if df_activos.empty:
        st.warning("No hay casos activos cargados.")
    else:
        st.dataframe(df_activos.head(), use_container_width=True)


# ============================================================
# CASOS ACTIVOS
# ============================================================

elif opcion == "Casos activos":
    st.subheader("Casos activos")

    if df_activos.empty:
        st.warning("No hay casos activos cargados.")
    else:
        st.dataframe(df_activos, use_container_width=True)


# ============================================================
# BUSCAR CASO ESPECÍFICO
# ============================================================

elif opcion == "Buscar caso específico":
    st.subheader("Buscar caso específico")

    nombre_buscado = st.text_input(
        "Ingresá el nombre y apellido exacto",
        placeholder="Ejemplo: Juan Pérez"
    )

    if st.button("Buscar"):
        try:
            nombre_validado = validar_nombre_apellido(nombre_buscado.strip())
            resultado = filtrar_participante(df_activos, nombre_validado)

            if resultado.empty:
                st.warning("No se encontraron registros con ese nombre.")
            else:
                st.success("Caso encontrado.")
                st.dataframe(resultado, use_container_width=True)

        except ValueError as e:
            st.error(str(e))

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")


# ============================================================
# AGREGAR NUEVO CASO
# ============================================================

elif opcion == "Agregar nuevo caso":
    st.subheader("Agregar nuevo caso")

    with st.form("formulario_agregar_caso"):
        nombre = st.text_input("Nombre y Apellido")
        edad = st.text_input("Edad")
        genero = st.text_input("Género")
        peso = st.text_input("Peso (kg)")
        altura = st.text_input("Altura (m)")
        rasgos = st.text_area("Rasgos Físicos")
        zona = st.text_input("Zona (Argentina)")
        datos_extra = st.text_area("Datos Extra")

        enviar = st.form_submit_button("Guardar caso")

    if enviar:
        try:
            nombre = validar_nombre_apellido(nombre.strip())
            edad = validar_entero_positivo(edad.strip(), "edad")
            genero = validar_texto_obligatorio(genero.strip(), "género")
            peso = validar_decimal_positivo(peso.strip(), "peso")
            altura = validar_decimal_positivo(altura.strip(), "altura")
            rasgos = validar_texto_obligatorio(rasgos.strip(), "rasgos físicos")
            zona = validar_texto_obligatorio(zona.strip(), "zona")
            datos_extra = validar_texto_obligatorio(datos_extra.strip(), "datos extra")

            df_actual = cargar_excel(ARCHIVO_ACTIVOS)

            for columna in COLUMNAS:
                if columna not in df_actual.columns:
                    df_actual[columna] = ""

            proximo_numero = obtener_proximo_numero_caso(df_actual)

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

            df_actual = pd.concat(
                [df_actual, pd.DataFrame([nueva_fila])],
                ignore_index=True
            )

            guardar_excel(df_actual, ARCHIVO_ACTIVOS)

            st.session_state["mensaje_exito"] = (
                f"El caso N° {proximo_numero} fue agregado correctamente."
            )
            st.rerun()

        except ValueError as e:
            st.error(str(e))

        except PermissionError:
            st.error("No se pudo guardar el archivo. Cerrá el Excel si está abierto.")

        except Exception as e:
            st.error(f"Ocurrió un error inesperado: {e}")


# ============================================================
# ESTADÍSTICAS Y GRÁFICOS
# ============================================================

elif opcion == "Estadísticas y gráficos":
    st.subheader("Estadísticas y gráficos")

    if df_activos.empty:
        st.warning("No hay datos para generar gráficos.")
    else:
        grafico = st.selectbox(
            "Elegí el gráfico que querés ver",
            [
                "Barras por zona",
                "Torta por género",
                "Histograma de edades",
                "Ver los 3 gráficos",
            ]
        )

        if grafico == "Barras por zona":
            st.write("Cantidad de casos por zona")
            mostrar_grafico_streamlit(grafico_barras_zona, df_activos)

        elif grafico == "Torta por género":
            st.write("Distribución de casos por género")
            mostrar_grafico_streamlit(grafico_torta_genero, df_activos)

        elif grafico == "Histograma de edades":
            st.write("Distribución de edades")
            mostrar_grafico_streamlit(grafico_histograma_edad, df_activos)

        elif grafico == "Ver los 3 gráficos":
            st.write("Cantidad de casos por zona")
            mostrar_grafico_streamlit(grafico_barras_zona, df_activos)

            st.write("Distribución de casos por género")
            mostrar_grafico_streamlit(grafico_torta_genero, df_activos)

            st.write("Distribución de edades")
            mostrar_grafico_streamlit(grafico_histograma_edad, df_activos)


# ============================================================
# MARCAR CASO COMO RESUELTO
# ============================================================

elif opcion == "Marcar caso como resuelto":
    st.subheader("Marcar caso como resuelto")

    if df_activos.empty:
        st.warning("No hay casos activos para modificar.")
    elif "N° Caso" not in df_activos.columns:
        st.error("No existe la columna 'N° Caso' en el archivo de casos activos.")
    else:
        casos_disponibles = df_activos["N° Caso"].dropna().tolist()

        numero_seleccionado = st.selectbox(
            "Seleccioná el número de caso",
            casos_disponibles
        )

        caso_seleccionado = df_activos[
            df_activos["N° Caso"] == numero_seleccionado
        ]

        st.write("Caso seleccionado:")
        st.dataframe(caso_seleccionado, use_container_width=True)

        confirmar = st.checkbox("Confirmo que quiero marcar este caso como resuelto")

        if st.button("Marcar como resuelto"):
            if not confirmar:
                st.error("Primero tenés que confirmar la acción.")
            else:
                try:
                    df_actual = cargar_excel(ARCHIVO_ACTIVOS)
                    df_resueltos_actual = cargar_excel(ARCHIVO_RESUELTOS)

                    caso = df_actual[df_actual["N° Caso"] == numero_seleccionado]

                    if caso.empty:
                        st.error("No se encontró un caso con ese número.")
                    else:
                        df_sin_caso = df_actual.drop(caso.index[0])

                        for columna in df_sin_caso.columns:
                            if columna not in df_resueltos_actual.columns:
                                df_resueltos_actual[columna] = ""

                        df_resueltos_actual = pd.concat(
                            [df_resueltos_actual, caso],
                            ignore_index=True
                        )

                        guardar_excel(df_sin_caso, ARCHIVO_ACTIVOS)
                        guardar_excel(df_resueltos_actual, ARCHIVO_RESUELTOS)

                        st.session_state["mensaje_exito"] = (
                            f"El caso N° {numero_seleccionado} fue marcado como resuelto."
                        )
                        st.rerun()

                except PermissionError:
                    st.error("No se pudo guardar el archivo. Cerrá el Excel si está abierto.")

                except Exception as e:
                    st.error(f"Ocurrió un error inesperado: {e}")


# ============================================================
# CASOS RESUELTOS
# ============================================================

elif opcion == "Casos resueltos":
    st.subheader("Casos resueltos")

    if df_resueltos.empty:
        st.warning("No hay casos resueltos todavía.")
    else:
        st.dataframe(df_resueltos, use_container_width=True)