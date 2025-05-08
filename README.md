General concept of the Project_movies project
This console application allows you to search for movies by various parameters in the database, show posters of the movies you like, and display the history of user queries.
________________________________________
🔍 Main file Project_movies
Acts as an entry point:
python
if __name__ == "__main__":
Starts a logical loop where the user:
1. Searches for movies;
2. Can view a poster;
3. Can view the query history.
________________________________________
📂 Imported modules and their functions:
________________________________________
1. search
from search import search_movies
📌 What search_movies() does:
• Asks the user for search parameters:
o genre, year, actor, minimum rating, keywords;
• Generates an SQL query based on these parameters;
• Searches for movies in the database;
• Saves the query to the log (queries table);
• Returns a list of found movies.
________________________________________

2. poster
from poster import show_movie_poster
📌 What show_movie_poster() does:
• Asks the user for the movie ID;
• Query the database to get the link to the poster;
• If the poster is found, displays it via IPython.display.Image;
• If not, prints a message that the poster is missing.
________________________________________
3. history
from history import print_log_history
📌 What print_log_history() does:
• Connects to the local database;
• Retrieves the history of all user queries;
• Prints them as a table using tabulate;
• Allows the user to analyze previous searches.
________________________________________
4. front
import front
📌 What front.print_results(...) does:
• This is a helper function for printing movie results in a pretty way:
o Sorts, formats, or displays the results in a table;
• If you output via print(row), then front.print_results() is a more convenient and pleasant way for the user.
________________________________________
