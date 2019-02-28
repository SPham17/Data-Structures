"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Steven Pham
ID:      180198020
Email:   pham8020@mylaurier.ca
Section: CP164 A
__updated__ = "2019-01-08"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    m_title = input("Title: ")
    m_year = int(input("Year: "))
    m_director = input("Director: ")
    m_rating = float(input("Rating: "))
    m_genres = int(input("Genres:"))

    the_genres = []
    the_genres.append(m_genres)
    
    movie = Movie(m_title, m_year, m_director, m_rating, the_genres)

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    line = line.split("|")

    genre = []

    string_genre = line[4]

    for i in range (len(string_genre)):
        if string_genre[i].isdigit():
            value = int(string_genre[i])
            genre.append(value)

    #create the movie object
    movie = Movie(line[0],int(line[1]),line[2],float(line[3]),genre)


    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies = [] #list of movie obj
    
    fv.seek(0)
    
    line = fv.readline() 
    
    #keep going till end
    while(line != ""):
        movie_object = read_movie(line)
        movies.append(movie_object)
        line = fv.readline()

    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """
    for x in range(len(Movie.GENRES)):
        print("{}: {}".format(x,Movie.GENRES[x]))

    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    genre_number = input("Enter a genre number (ENTER to quit): ")


    choice = True

    while choice:
    
        if len(genres) != 0 and genre_number == "":
            choice = False
        
        elif len(genres) == 0 and genre_number == "":
            print("Error: not a positive number.")
            genre_number = input("Enter a genre number (ENTER to quit): ") 
        
        elif genre_number.isalpha() == True:
            print("Error: not a positive number.")
            genre_number = input("Enter a genre number (ENTER to quit): ") 
        
        elif int(genre_number) < 0:
            print("Error: not a positive number.")
            genre_number = input("Enter a genre number (ENTER to quit): ") 
        
        elif int(genre_number) > 10:
            print("Error: input must be < 10")
            genre_number = input("Enter a genre number (ENTER to quit): ") 
    
        else:
            genres.append(genre_number)
            genre_number = input("Enter a genre number (ENTER to quit): ") 
    
        for x in range(len(genres)):
            if genre_number == genres[x]:
                print("Error: genre already chosen")
                genres.pop()
            
    genres = [int(i) for i in genres]
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    
    ymovies = []
    
    for x in movies:
        # loops thru obj list
        if x.year == year:
            #specifically looks for the yr of the movie obj and when it matches the user input, it will append into a diff list
            ymovies.append(x)
            
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = []
    
    for x in movies:
        if x.rating == rating:
            rmovies.append(x)

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    
    for x in movies:
        if genre in x.genres:
            gmovies.append(x)

    return gmovies

def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    
    for x in movies:
        if x.genres == genres:
            gmovies.append(x)

    return gmovies

def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    
    SCIFI = 0
    FANTASY = 0 
    DRAMA = 0
    ROMANCE = 0
    COMEDY = 0
    ZOMBIE = 0 
    ACTION = 0
    HISTOR = 0
    HORROR = 0
    WAR = 0
    
    for i in movies:
        if 0 in i.genres:
            SCIFI += 1
        if 1 in i.genres:
            FANTASY += 1
        if 2 in i.genres:
            DRAMA += 1
        if 3 in i.genres:
            ROMANCE += 1
        if 4 in i.genres:
            COMEDY += 1
        if 5 in i.genres:
            ZOMBIE += 1
        if 6 in i.genres:
            ACTION += 1
        if 7 in i.genres:
            HISTOR += 1
        if 8 in i.genres:
            HORROR += 1
        if 9 in i.genres:
            WAR += 1
   
    counts.append(SCIFI)
    counts.append(FANTASY)
    counts.append(DRAMA)
    counts.append(ROMANCE)
    counts.append(COMEDY)
    counts.append(ZOMBIE)
    counts.append(ACTION)
    counts.append(HISTOR)
    counts.append(HORROR)
    counts.append(WAR)

    return counts
