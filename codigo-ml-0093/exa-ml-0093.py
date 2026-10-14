import sys
import os
import pandas as pd

# Permitir importar dicc_0093.py desde la subcarpeta hermana datos-de-entrada-ml-0093 o la raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0093')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dicc_0093

print("Pedro Martinez Machine Learning pandas, NC 0093")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Pedro Martinez Machine Learning pandas, NC 0093"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame (usando datos_laboratorios)
df = pd.DataFrame(dicc_0093.datos_laboratorios)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Equipos)
registrar("3. Estadísticas Generales de la Columna 'Equipos'", df['Equipos'].describe())

# 4. Ordenar Ascendente por Equipos
df_asc_equipos = df.sort_values(by="Equipos", ascending=True)
registrar("4. Ordenar Ascendente por Equipos", df_asc_equipos)

# 5. Ordenar Descendente por Investigadores
df_desc_investigadores = df.sort_values(by="Investigadores", ascending=False)
registrar("5. Ordenar Descendente por Investigadores", df_desc_investigadores)

# 7. Guardar el archivo resultados-ml-0093.md dentro de resultados-0093
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0093'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0093.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Pedro Martinez Machine Learning pandas, NC 0093")