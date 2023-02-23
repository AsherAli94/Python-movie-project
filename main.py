# Created by : Asher Ali
# Dated: 23.02.2023
# Movie project


MENU_PROMPT = "\nEnter 'a' to add a movie , 'l' to see your movies, 'f' to find a movie by title and 'q' to quit: "
movies = []

def Get_User_Input():
    title = input("\nEnter the movie title: ")
    director = input("\nEnter the movie director: ")
    year = input("\nEnter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def List_All_Movies():
    for movie in movies:
        print(movie)

def Find_Movie_By_Title(title):
    for movie in movies:
        if movie['title'] == title:
            print(movie)
            return 1
    return 0

"""
def User_Menu():
    while 1:
        selection = input(MENU_PROMPT)
        if selection == 'q':
            break
        elif selection == 'a':
            Get_User_Input()
        elif selection == 'l':
            List_All_Movies()
        elif selection == 'f':
            title = input("\nEnter the title: ")
            if Find_Movie_By_Title(title) == 0:
                print("\nNo movie found with the title ")
        else:
           print("\nPlease enter a valid command")
"""

# Usage of first class functions as well
user_options = {
    "a": Get_User_Input,
    "l": List_All_Movies,
    "f": Find_Movie_By_Title
}

def User_Menu():
    while 1:
        selection = input(MENU_PROMPT)
        if selection == 'q':
            break
        elif selection in user_options:
            if selection == 'f':
                title = input("\nEnter the title: ")
                selected_func = user_options[selection]
                if selected_func(title) == 0:
                    print("\nNo movie found with the title ")
                continue
            selected_func = user_options[selection]
            selected_func()
        else:
           print("\nPlease enter a valid command")

User_Menu()