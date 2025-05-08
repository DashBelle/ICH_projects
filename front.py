from tabulate import tabulate

def print_results(results):
    if results:
        print('Search results:')
        columns = ['Title', 'Year', 'Rating', 'Genres', 'Runtime']
        print(tabulate(results, columns, 'grid'))
    else:
        print('Nothing found')
