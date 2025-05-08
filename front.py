from tabulate import tabulate

def print_results(results):
    if results:
        print('Результаты поиска:')
        columns = ['Title', 'Year', 'Rating', 'Genres', 'Runtime']
        print(tabulate(results, columns, 'grid'))
    else:
        print('Ничего не нашлось')