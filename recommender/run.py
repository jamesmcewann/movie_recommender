import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os
import random

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

def evaluate_movie(df, movie):
    print('evaluating movie')
    usr_input = 0
    while usr_input != 3:
        print(f"""==================================
{{{movie['Series_Title']}}}
1. Roll Again
2. Add to Watched List
3. Return to main menu
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
                    print('Watched!')
                    break
                case 3:
                    break
                case _:
                    print("Invalid input. Try again.")
        except ValueError as e:
            print("Enter valid number option 1, 2, 3 or 4")
            continue

def menu(df):

    usr_input = 0
    while usr_input != 4:
        print("""==================================
Welcome to the Recommender System
1. Lucky Dip
2. Record Watched Movies
3. Recommend Movies
4. Exit
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
                    pass
                case 3:
                    pass
                case 4:
                    print("Exiting...")
                case _:
                    print("Invalid input. Try again.")
        except ValueError as e:
            print("Enter valid number option 1, 2, 3 or 4")
            continue
    
def main():
    path = download_dataset()
    df = get_dataframe(path) 

    menu(df)

if __name__ == "__main__":
    main()
 