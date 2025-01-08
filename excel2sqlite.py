import pandas as pd
import sqlite3
import sys

def excel_to_sqlite(excel_file, sheet_name, database_name, table_name):
    # Leer los datos del fichero Excel
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    # Conectar o crear la base de datos SQLite
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        print(f"Conectado a la base de datos '{database_name}'.")
    except Exception as e:
        print(f"Error al conectar con la base de datos SQLite: {e}")
        return

    # Crear la tabla (si no existe) basándose en el DataFrame
    try:
        # Insertar los datos del DataFrame en la base de datos
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Datos insertados en la tabla '{table_name}' de la base de datos '{database_name}'.")
    except Exception as e:
        print(f"Error al insertar datos en SQLite: {e}")
    finally:
        # Cerrar la conexión
        conn.close()
        print("Conexión a la base de datos cerrada.")

# Ejemplo de uso
if __name__ == "__main__":
    for arg in sys.argv: 
        print(arg)




    #excel_file = ARGUMENTO1  # Ruta al fichero Excel
    #sheet_name = HOJA         # Nombre de la hoja en el Excel
    #database_name = BBDD  # Nombre del archivo de base de datos SQLite
    #table_name = TABLA   # Nombre de la tabla donde se insertarán los datos

    #excel_to_sqlite(excel_file, sheet_name, database_name, table_name)