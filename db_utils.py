import mysql.connector
from db_config import get_dbconfig

def connect_to_database(host, user, password, database, port):
    return mysql.connector.connect(
        host=host, user=user, password=password,
        database=database, port=port
    )

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {str(e)}")
        return None
    finally:
        cursor.close()
        connection.close()

def insert_query(log):
    try:
        conn = connect_to_database(**get_dbconfig(True))
        cursor = conn.cursor()
        cursor.execute('INSERT INTO queries (query) VALUES (%s)', (log,))
        conn.commit()
        print("✅ Запрос записан.")
    except Exception as e:
        print(f'❌ Ошибка записи: {str(e)}')
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals() and conn.is_connected(): conn.close()