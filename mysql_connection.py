import pymysql as mysql
import pandas as pd
from dotenv import load_dotenv 
import os

## Cargo las variables de entorno
load_dotenv('.env') # Cargo la archivo donde esta la variable de entorno.
mysql_key = '1533542415'
##################  MYSQL   ##################
def get_connection_mysql():
    """
    Esta funcion se conecta a la base de datos establecida en amazon, y coenca la base de datos QUANTYLE_ANALITICS

    Returns:
        conexion:Retorna un objeto conexion, para realizar peticiones a la base de datos.
    """
    
    try:
        return mysql.connect(host = 'servidorgrupo.cpfbmucjyznh.us-east-2.rds.amazonaws.com',
                         user = 'admin',
                         password = mysql_key,
                         port=3306,
                         database='quantyle')
    except mysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise  # Re-levanta la excepción para que el código que llama pueda manejarla si es necesario
    

def get_table(table_name):
    """
    Esta funcion aplica la funcion mysql_get_connection, y devuelve una tabla de la base de datos en formato dataframe de pandas.
    

    Args:
        table_name (string): Nombre de la tabla requerida en la base de datos.

    Returns:
        pd.DataFrame: Data Frame de la tabla table_name.
    """
    conexion = get_connection_mysql()
    try:
        # Iniciar conexión a MySQL
        cursor = conexion.cursor()
        consulta = f"SELECT * FROM {table_name}"
        cursor.execute(consulta)
        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()
        # Obtener los nombres de las columnas
        columnas = [columna[0] for columna in cursor.description]
        # Crear un DataFrame de Pandas con los resultados y los nombres de las columnas
        df = pd.DataFrame(resultados, columns=columnas)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cerrar la conexión a MySQL en cualquier caso
        cursor.close()
    return df




def get_filtered_table(table_name, id_list):
    """
    Esta función aplica la función mysql_get_connection y devuelve una tabla de la base de datos
    en formato DataFrame de Pandas, filtrada por una lista de IDs.

    Args:
        table_name (string): Nombre de la tabla requerida en la base de datos.
        id_list (list): Lista de IDs para filtrar la tabla.

    Returns:
        pd.DataFrame: DataFrame de la tabla table_name filtrada por los IDs proporcionados.
    """
    if not id_list:
        return pd.DataFrame()  # Si la lista de IDs está vacía, retorna un DataFrame vacío
    
    # Convertir la lista de IDs en un string separado por comas para usar en el query SQL
    id_string = ','.join(map(str, id_list))

    conexion = get_connection_mysql()
    try:
        # Iniciar conexión a MySQL
        cursor = conexion.cursor()
        consulta = f"SELECT * FROM {table_name} WHERE user_id IN (%s)"
        cursor.executemany(consulta,id_list)
        
        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()
        
        # Obtener los nombres de las columnas
        columnas = [columna[0] for columna in cursor.description]
        
        # Crear un DataFrame de Pandas con los resultados y los nombres de las columnas
        df = pd.DataFrame(resultados, columns=columnas)
    except Exception as e:
        print(f"Error: {e}")
        df = pd.DataFrame()  # Retorna un DataFrame vacío en caso de error
    finally:
        # Cerrar la conexión a MySQL en cualquier caso
        cursor.close()
    return df

##################  MYSQL   ##################