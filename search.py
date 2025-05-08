from db_utils import connect_to_database, execute_query, insert_query
from db_config import get_dbconfig

def search_movies():
    genre = input('Введите жанр [Action, Drama, Comedy и т.д.] (или оставьте поле пустым):')
    year = input('Введите год [2007 - 2015] (или оставьте поле пустым):')
    actor = input('Введите актера (или оставьте поле пустым):')
    rating = input('Введите минимальный рейтинг (или оставьте поле пустым):')
    keywords = input('Введите ключевые слова (или оставьте поле пустым)')

    conditions = [
        f"genres LIKE '%{genre}%'" if genre else "1",
        f"year LIKE '%{year}%'" if year else "1",
        f"cast LIKE '%{actor}%'" if actor else "1",
        f"(title LIKE '%{keywords}%' OR plot LIKE '%{keywords}%')" if keywords else "1"
    ]

    if rating:
        conditions.append(f"`imdb.rating` >= {rating}")

    query = f"""
    SELECT id, title, year, `imdb.rating`, genres, runtime FROM movies
    WHERE {' AND '.join(conditions)}
    ORDER BY `imdb.rating` DESC
    """

    log_parts = [
        f'genres: {genre}', f'year: {year}', f'actor: {actor}',
        f'rating: {rating}', f'keywords: {keywords}'
    ]
    log = ' | '.join(filter(None, log_parts))
    if log:
        insert_query(log)

    conn = connect_to_database(**get_dbconfig(False))
    return execute_query(conn, query)