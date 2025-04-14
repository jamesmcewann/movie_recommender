import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os
import random
import sys
import json
from movie import Movie

def initialise():
    if os.path.exists(os.path.join(os.getcwd(), 'save_data', 'users.json')):
        print("Initialised")
    else:
        with open(os.path.join(os.getcwd(), 'save_data', 'users.json'), 'w') as file:
            json_data = {
                "users": []
            }
            file.write(json.dumps(json_data, indent=4))

def login():
    username_input = ""
    password_input = ""
    password_attempts = 0
    while username_input != "exit":
        username_input = input("Enter your username: ")
        with open(os.path.join(os.getcwd(), 'save_data', 'users.json'), 'r') as file:
            data = json.load(file)
            for user in data['users']:
                if user['username'] == username_input.strip():
                    while password_input != "exit":
                        password_input = input("Enter your password: ")
                        if user['password'] == password_input:
                            print("Login successful")
                            return True
                        else:
                            password_attempts += 1
                            print(f"Incorrect password. Attempts: {password_attempts} - Try again.")
                            if password_attempts >= 3:
                                sys.exit("Too many attempts. Try again later.")
                            continue
                    sys.exit("Exiting...")
            print("Username not found. Try again.")
    sys.exit("Exiting...")

def register():
    username_input = ""
    password_input = ""
    while username_input != "exit":
        username_input = input("Enter your username: ")
        with open(os.path.join(os.getcwd(), 'save_data', 'users.json'), 'r') as file:
            data = json.load(file)

        for user in data['users']:
            if user['username'] == username_input.strip():
                print("Username already exists. Try again.")
                break
            else:
                password_reinput = ""
                password_input = input("Enter your password: ")
                while password_input != password_reinput:
                    password_reinput = input("Re-enter your password: ")
                    if password_input == password_reinput:
                        print("Registration successful")
                        with open(os.path.join(os.getcwd(), 'save_data', 'users.json'), 'w') as write_file:
                            new_user = {
                                "username": username_input,
                                "password": password_input
                            }
                            data['users'].append(new_user)
                            json.dump(data, write_file, indent=4)
                            return True
                    else:
                        print("Passwords do not match. Try again.")
                        break
    sys.exit("Exiting...")


def welcome_screen():
    usr_input = 0
    while usr_input != 3:
        print('''========================================
Welcome to the Movie Recommender System'
========================================
1. Login 
2. Register
3. Exit
========================================''')
        usr_input = int(input("Enter your choice: "))
        match usr_input:
            case 1:
                print("Login")
                login()
                break
            case 2:
                print("Register")
                register()
                break
            case 3:
                sys.exit("Exiting...")
            case _:
                print("Invalid input. Try again.")

def download_dataset():
    path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
    print('Path to dataset files: ', path)
    return path

def get_dataframe(path):
    path = os.path.join(path, 'imdb_top_1000.csv')
    df = pd.read_csv(path)
    return df

def lucky_dip(df):
    rdm_int = random.randint(0, 1000)
    print(type(df.iloc[rdm_int]))
    return df.iloc[rdm_int]

def add_watched(df, movie):
    watched_movie = Movie(movie)
    watched_movie.update_watched()
    while True:
        try:
            usr_input = int(input("Give a rating 1-5: "))
            if usr_input > 5 or usr_input < 0:
                raise ValueError
            else:
                watched_movie.update_rating(usr_input)
                return
        except ValueError as e:
            print("Enter valid rating 1-5")
            continue

def add_to_watchlist(df, movie):
    to_watch_movie = Movie(movie)
    to_watch_movie.update_to_watch()
    return

def evaluate_movie(df, movie):
    print('evaluating movie')
    usr_input = 0
    while usr_input != 3:
        print(f"""==================================
{{{movie['Series_Title']}}}
1. Roll Again
2. Add to Watched List
3. Add to To-Watch List
4. Return to main menu
==================================
""")
        try:
            usr_input = int(input("Enter your choice: "))
            match usr_input:
                case 1:
                    new_movie = lucky_dip(df)
                    print(new_movie)
                    evaluate_movie(df, new_movie)
                    break
                case 2:
                    add_watched(df, movie)
                    break
                case 3:
                    add_to_watchlist(df, movie)
                    break
                case 4:
                    break
                case _:
                    print("Invalid input. Try again.")
        except ValueError as e:
            print("Enter valid number option 1, 2, 3 or 4")
            continue

def menu(df):

    usr_input = 0
    while usr_input != 6:
        print("""==================================
Welcome to the Recommender System
1. Lucky Dip
2. Record Watched Movies
3. View Watched Movies
4. View To-Watch List
5. Recommend Movies
6. Exit
==================================
""")
        try:
            usr_input = int(input("Enter your choice: "))
            match usr_input:
                case 1:
                    movie = lucky_dip(df)
                    print(movie)
                    evaluate_movie(df, movie)
                case 2:
                    print("Record Watched Movies")
                    pass
                case 3:
                    print("View Watched Movies")
                    pass
                case 4:
                    print("View To-Watch List")
                    pass
                case 5:
                    print("Recommend Movies")
                    pass
                case 6:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid input. Try again.")
        except ValueError as e:
            print("Enter valid number option 1, 2, 3 or 4")
            continue
    
def main():
    path = download_dataset()
    df = get_dataframe(path) 

    initialise()
    #login()
    #login = input("Enter your name: ")

    welcome_screen()
    menu(df)

if __name__ == "__main__":
    main()
 

 