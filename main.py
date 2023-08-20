#import json
#file_path = "movies.json"
#with open(file_path, "r") as json_file:
#    movies = json.load(json_file)
#print(movies)
# task 3
import json


# file_path = "movies.json"

#
# with open(file_path, "r") as json_file:
#     data = json.load(json_file)
#
# movies_list = data["movies"]
#
# formatted_output = ""
# for movie in movies_list:
#     formatted_output += f"Movie name is {movie['Movie name']}. Its genre is {', '.join(movie['Genre'])}. "
#     formatted_output += f"The runtime of the movie is {movie['Runtime']} seconds. The Metascore for the movie is {movie['Metascore']}. "
#     formatted_output += f"The IMDb rating is {movie['IMDb ratings']}. The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
#     formatted_output += f"The release date of the movie is {movie['Release date']} (Unix timestamp).\n\n"
#
#
# print(formatted_output)
# task4
# import json
#
# file_path = "movies.json"
#
#
# with open(file_path, "r") as json_file:
#     data = json.load(json_file)
#
# movies_list = data["movies"]
#
#
#
# def add_movie():
#     movie = {}
#     movie["Movie name"] = input("Enter the movie name: ")
#     genres = input("Enter genres: ").split(",")
#     movie["Genre"] = [genre.strip() for genre in genres]
#     movie["Runtime"] = int(input("Enter the runtime of the movie: "))
#     movie["Metascore"] = int(input("Enter the Metascore for the movie: "))
#     movie["IMDb ratings"] = float(input("Enter the IMDb rating for the movie: "))
#     lead_actors = input("Enter lead actors are: ").split(",")
#     movie["Lead actors"] = [actor.strip() for actor in lead_actors]
#     movie["Release date"] = int(input("Enter the release date of the movie is: "))
#
#     movies_list.append(movie)
#     print("Movie added successfully!\n")
#
# def display_movies():
#     formatted_output = ""
#     for movie in movies_list:
#         formatted_output += f"Movie name is {movie['Movie name']}. Its genre is {', '.join(movie['Genre'])}. "
#         formatted_output += f"The runtime of the movie is {movie['Runtime']} seconds. The Metascore for the movie is {movie['Metascore']}. "
#         formatted_output += f"The IMDb rating is {movie['IMDb ratings']}. The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
#         formatted_output += f"The release date of the movie is {movie['Release date']} .\n\n"
#     print(formatted_output)
#
# while True:
#     print("1. Display Movies")
#     print("2. Add a new Movie")
#     print("3. Exit")
#
#     choice = input("Enter your choice (1/2/3): ")
#
#     if choice == "1":
#         display_movies()
#     elif choice == "2":
#         add_movie()
#     elif choice == "3":
#
#         data["movies"] = movies_list
#         with open(file_path, "w") as json_file:
#             json.dump(data, json_file, indent=4)
#         break
#     else:
#         print("Invalid choice. Please try again.\n")
# 5tH TASK

import json

# file_path = "movies.json"
#
# def add_new_movie():
#     movie = {}
#     movie["Movie name"] = input("Enter the movie name: ")
#     genres = input("Enter genres (separated by commas): ").split(",")
#     movie["Genre"] = [genre.strip() for genre in genres]
#     movie["Runtime"] = int(input("Enter the runtime of the movie is "))
#     movie["Metascore"] = int(input("Enter the Metascore for the movie: "))
#     movie["IMDb ratings"] = float(input("Enter the IMDb rating for the movie: "))
#     lead_actors = input("Enter lead actors  ").split(",")
#     movie["Lead actors"] = [actor.strip() for actor in lead_actors]
#     movie["Release date"] = int(input("Enter the release date of the movie  "))
#
#     with open(file_path, "r") as json_file:
#         data = json.load(json_file)
#
#     movies_list = data["movies"]
#     movies_list.append(movie)
#
#     with open(file_path, "w") as json_file:
#         json.dump(data, json_file, indent=4)
#
#     print("Movie added successfully!")
#
# def display_movies():
#     with open(file_path, "r") as json_file:
#         data = json.load(json_file)
#
#     formatted_output = ""
#     for movie in data["movies"]:
#         formatted_output += f"Movie name is {movie['Movie name']}. Its genre is {', '.join(movie['Genre'])}. "
#         formatted_output += f"The runtime of the movie is {movie['Runtime']} seconds. The Metascore for the movie is {movie['Metascore']}. "
#         formatted_output += f"The IMDb rating is {movie['IMDb ratings']}. The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
#         formatted_output += f"The release date of the movie is {movie['Release date']}.\n\n"
#     print(formatted_output)
#
# while True:
#     print("1. Display Movies")
#     print("2. Add a new Movie")
#     print("3. Delete a Movie")
#     print("4. Exit")
#
#     choice = input("Enter your choice (1/2/3/4): ")
#
#     if choice == "1":
#         display_movies()
#     elif choice == "2":
#         add_new_movie()
#     elif choice == "3":
#         movie_name = input("Enter the name of the movie you want to delete: ")
#         delete_movie(movie_name)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice. Try again.\n")
import json
from datetime import datetime

file_path = "movies.json"


def read_write_json(data=None, write=False):
    if write:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    else:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data


def get_movie_input():
    movie = {}
    movie_name = input("Enter the movie name: ")

    movie["Movie name"] = movie_name
    genres = input("Enter genres: ").split(",")
    movie["Genre"] = [genre.strip() for genre in genres]
    movie["Runtime"] = int(input("Enter the runtime of the movie in seconds: "))
    movie["Metascore"] = int(input("Enter the Metascore for the movie: "))
    movie["IMDb ratings"] = float(input("Enter the IMDb rating for the movie: "))
    lead_actors = input("Enter lead actors: ").split(",")
    movie["Lead actors"] = [actor.strip() for actor in lead_actors]
    release_date_str = input("Enter the release date of the movie (DD-MM-YYYY): ")
    release_date = datetime.strptime(release_date_str, "%d-%m-%Y")
    movie["Release date"] = int(release_date.timestamp())

    return movie


def add_new_movie(movie):
    data = read_write_json()
    movie_name = movie["Movie name"].lower()

    movies_list = data["movies"]
    for existing_movie in movies_list:
        if existing_movie["Movie name"].lower() == movie_name.lower():
            print("Movie with the same name already exists.")
            return

    movies_list.append(movie)
    read_write_json(data, write=True)
    print("Movie added successfully!")

def get_formatted_datetime(epoch_time):
    dt_object = datetime.fromtimestamp(epoch_time)
    formatted_datetime = dt_object.strftime("%d-%m-%Y")
    return formatted_datetime


def display_movies():
    data = read_write_json()
    formatted_output_strings = [
        f"Movie name is {movie['Movie name']}. "
        f"Its genre is {', '.join(movie['Genre'])}."
        f" The runtime of the movie is {movie['Runtime']} seconds. "
        f"The Metascore for the movie is {movie['Metascore']}. "
        f"The IMDb rating is {movie['IMDb ratings']}. "
        f"The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
        f"The release date of the movie is {get_formatted_datetime(movie['Release date'])}.\n"
        for movie in data["movies"]
    ]
    formatted_output = "\n".join(formatted_output_strings)
    print(formatted_output)


def delete_movie(movie_name):
    data = read_write_json()
    movies_list = data["movies"]
    found = False

    for movie in movies_list:
        if movie["Movie name"].lower() == movie_name.lower():
            movies_list.remove(movie)
            found = True
            break

    return found


def main():
    while True:
        print("1. Display Movies")
        print("2. Add a new Movie")
        print("3. Delete a Movie")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_movies()
        elif choice == "2":
            movie =get_movie_input()
            add_new_movie(movie)
        elif choice == "3":
            movie_name = input("Enter the name of the movie you want to delete: ")
            found = delete_movie(movie_name)

            if found:
                print("Movie deleted successfully!")
            else:
                print("Movie not found.")
        elif choice == "4":
            break
        else:
            print("Invalid. Try again.\n")


if __name__ == "__main__":
    main()
