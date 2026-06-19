# TP_Aplicado
Sistema de Gestión y Monitoreo de Personas Desaparecidas

1. Autoras del proyecto
- Miranda Berazategui
- Catalina Hawes
- Sofia Jalil
- Guadalupe Merke
- Matilde Nuñez

2. Objetivo y descripción general del proyecto
  El objetivo principal de este proyecto es ayudar a centralizar y difundir información clara y actualizada sobre personas que están desaparecidas o que ya fueron encontradas. 

2.1 Funcionalidades
  La plataforma fue pensada como una herramienta práctica para manejar estos datos de forma ordenada a través de tres funciones clave. Por un lado, el sistema permite hacer consultas rápidas, ofreciendo la opción de ver la lista completa de todos los casos activos o buscar directamente a una persona en específico para ver su ficha detallada. Por otro lado, facilita el día a día de la gestión operativa, ya que se pueden cargar nuevos reportes de manera controlada y actualizar el estado de los casos cuando se resuelven, pasándolos automáticamente a un archivo histórico para mantener la base activa limpia y al día. Por último, sumamos un módulo de estadísticas que transforma todos estos datos en gráficos fáciles de leer, lo que ayuda un montón a identificar patrones y ver de un vistazo información clave, como la cantidad de casos distribuidos por zona, edad o sexo.

2.2 Adjudicación de Roles

Mirand berazategui
- Función que modifica el estado de un caso
- Función validacion
- Streamlit
- Diseño

Matilde Nuñez
- Función mostrar un caso específico solicitado
- Diseño

Catalina Hawes 
- Función que muestra todo el archivo
- Función que muestra casos resueltos 
- Código principal
- Diseño
- Readme

Sofia Jalil Bestard 
- Función que muestra los gráficos
- Código principal 
- Corregir errores
- Diseño

Guadalupe Merke
- Agregar nuevo caso
- Diseño
- Presentacion visual

3. Descripción de la fuente de datos

El programa recibe un excel que contiene los siguientes datos:
- Nombre y Apellido
- Edad
- Género
- Peso (en kg)
- Altura (en metros)
- Rasgos físicos (color de pelo, color de ojos y color de tez)
- Zona
- Datos extra (por ejemplo qué ropa tenía al momento de la desaparición, si tiene tatuajes, etc)

4. Instrucciones para ejecutar el programa
	Para poder correr el programa, el usuario debe clonar el github en su aplicación; lo que permitirá que pueda acceder a todos los archivos que se requieren para el trabajo. Luego, se deben abrir (en Python) el archivo principal y todos aquellos archivos que se encuentren dentro de la carpeta Src. Y por último, debe correr el programa desde el main.

5. Librerías Utilizadas
- pandas: utilizada para la manipulación eficiente de estructuras de datos, lectura, escritura y actualización de los archivos Excel como DataFrames.
- os: utilizada para la gestión de rutas del sistema operativo y resolución de compatibilidad de archivos de manera multiplataforma.
- streamlit (Módulo Dashboard): utilizada para el despliegue de la interfaz web dinámica e interactiva final.

6. Estructura del Repositorio

Estructura del Repositorio
├── Datos/
│   ├── informacion_usuarios.xlsx
│   └── Casos resueltos.xlsx
├── Src/
│   ├── Funcion_general.py
│   ├── modificar_caso_resuelto.py
│   ├── agregar_caso.py
│   ├── funcion_graficos.py
│   ├── mostrar_resueltos.py
│   ├── filtrar_por_desaparecido_especifico.py
│   └── funcion_validacion.py
├── Principal.py
├── Diseño/
│   └── [Diagramas de flujo y documentación]
├── requirements.txt
├── README.md
└── app.pys Funciones Principales

1) Visualización del Registro General
- Función: lectura completa del archivo.
- Descripción: el sistema accede al excel principal que almacena la totalidad de los registros históricos, procesa las líneas de datos y las despliega de forma ordenada en la consola para permitir una auditoría visual de todos los casos vigentes.

2) Búsqueda y Filtrado de Casos Particulares
- Función: consulta al usuario el nombre de la persona que quiere saber.
- Descripción: el programa solicita al operador el ingreso de un nombre específico. Posteriormente, ejecuta un algoritmo de búsqueda para identificar coincidencias dentro del archivo general. Al hallar el registro, extrae la línea de información correspondiente y la imprime de manera exclusiva en la consola.

3) Alta de Nuevos Registros
- Función: inserción y persistencia de datos en Hoja de Cálculo.
- Descripción: se pide al usuario la carga parametrizada de todas las variables obligatorias que componen la estructura de un caso. Una vez validados los campos, el programa realiza una operación de escritura (append) para añadir esta nueva fila al archivo Excel de base.

4) Módulo de Análisis Estadístico y Visualización
- Función: procesamiento de datos y generación de gráficos.
- Descripción: el submenú interroga al usuario sobre la variable demográfica o geográfica que desea analizar. El sistema segmenta la base de datos y genera representaciones gráficas dinámicas (gráficos de barras, torta, etc.) para exponer variables críticas como la distribución de casos por zona, sexo o rango etario.

5) Actualización de Estado (Flujo de Proceso a Resuelto)
- Función: migración y depuración de registros inter-archivos.
- Descripción: permite cambiar el estatus de un caso activo a "Resuelto". El usuario introduce el número de caso que fue resuelto; el sistema localiza la línea en el archivo general, la elimina para evitar duplicidades en la base activa, y la transfiere de manera íntegra a un archivo secundario destinado exclusivamente al historial de casos concluidos.

6) Auditoría del Histórico de Casos Resueltos
- Función: lectura del archivo con los casos resueltos.
- Descripción: utiliza la misma lógica de lectura de la Opción 1, pero redirige el canal de entrada hacia el archivo secundario de casos resueltos. Permite constatar de forma aislada el registro de todos los éxitos y cierres formales del sistema.

8. Resultados y Funcionalidades Generadas
  Como resultado de su ejecución, el programa logra procesar la base de datos de manera eficiente para ofrecer tres salidas principales al usuario:
- En primer lugar, genera visualizaciones completas y ordenadas en pantalla de los archivos de datos, permitiendo visualizar tanto la lista de personas que continúan desaparecidas como el registro histórico de aquellas que ya fueron encontradas. 
- En segundo lugar, el sistema es capaz de filtrar toda la base para devolver de forma exclusiva la información detallada de una persona en específico tras realizar una búsqueda. 
- Por último, el programa procesa los datos recopilados y los transforma en estadísticas visuales, mostrando diferentes tipos de gráficos que reflejan información clave y de gran utilidad para el análisis de los casos.

9. Declaración de uso de IA
- Creación del archivo: se solicitó la estructura de una hoja de cálculo en formato Excel con datos inventados (aleatorios). Este se realizó siguiendo los lineamientos y las categorías pedidas.

- Corrección de errores: una vez desarrollados los scripts iniciales, se procesaron los archivos a través de la IA para realizar una revisión de sintaxis y lógica. Este proceso permitió identificar fallas puntuales, comprender por qué surgieron mediante explicaciones y aplicar las correcciones sugeridas para garantizar la estabilidad del software.

- Unión de la arquitectura: dado que las funciones correspondientes a cada opción del menú se programaron de forma individual en archivos diferentes, se coordinó la integración de estos submódulos con el script principal (main). Esto aseguró una correcta importación de librerías y la continuidad en el flujo de ejecución del programa.

- Desarrollo del Dashboard: tras verificar el correcto funcionamiento de la lógica en consola, se procedió a la transición hacia una interfaz visual. Se adjuntan todos los códigos y se le pidió que realizara un código base en Streamlit. Siguiendo una guía de implementación paso a paso, se logró desplegar un tablero de control (dashboard) completamente interactivo y funcional.

- Optimización de estilo y claridad: Se utilizó la IA como herramienta de coedición para perfeccionar la redacción de la documentación del diseño y del archivo README. El objetivo principal fue estructurar la información de manera más profesional para asegurar que las ideas originales se transmitieran con total exactitud. Cabe destacar que no se delegó la redacción del contenido desde cero; en su lugar, se solicitó la reescritura y el pulido de los textos redactados por el equipo, transformando borradores propios en explicaciones más claras, fluidas y técnicamente precisas.

