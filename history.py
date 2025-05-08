from db_config import get_dbconfig
from tabulate import tabulate
import mysql.connector

def print_log_history():
    try:
        conn = mysql.connector.connect(**get_dbconfig(True))
        cursor = conn.cursor()
        cursor.execute("SELECT AD, query FROM queries ORDER BY AD DESC")
        rows = cursor.fetchall()
        if rows:
            print(tabulate(rows, headers=["ID", "Запрос"], tablefmt="grid"))
        else:
            print("⚠️ Нет сохранённых запросов.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals() and conn.is_connected(): conn.close()