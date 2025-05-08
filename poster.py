from db_config import get_dbconfig
from IPython.display import Image, display
import mysql.connector

def show_movie_poster():
    movie_id = input("Введите ID фильма: ").strip()
    try:
        conn = mysql.connector.connect(**get_dbconfig(False))
        cursor = conn.cursor()
        cursor.execute("SELECT poster FROM movies WHERE id = %s", (movie_id,))
        result = cursor.fetchone()

        if result and result[0]:
            print("🖼️ Постер:")
            display(Image(url=result[0]))
        else:
            print("⚠️ Постер не найден.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals() and conn.is_connected(): conn.close()