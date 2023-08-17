import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

file_path = "movies.json"


def read_write_json(data=None, write=False):
    if write:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    else:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data


def display_movies_gui():
    data = read_write_json()
    movies_data = data["movies"]

    movie_info = []
    for movie in movies_data:
        info = (
            f"Movie name: {movie['Movie name']}\n"
            f"Genre: {', '.join(movie['Genre'])}\n"
            f"Runtime: {movie['Runtime']} seconds\n"
            f"Metascore: {movie['Metascore']}\n"
            f"IMDb rating: {movie['IMDb ratings']}\n"
            f"Lead actors: {', '.join(movie['Lead actors'])}\n"
            f"Release date: {get_formatted_datetime(movie['Release date'])}\n\n"
        )
        movie_info.append(info)

    movie_info_text = "\n".join(movie_info)

    root = tk.Tk()
    root.title("Movie List")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_widget.insert(tk.INSERT, movie_info_text)
    text_widget.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


def main():
    while True:
        print("1. Display Movies")
        print("2. Add a new Movie")
        print("3. Delete a Movie")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_movies_gui()
        elif choice == "2":
            add_new_movie()
        elif choice == "3":
            movie_name = input("Enter the name of the movie you want to delete: ")
            delete_movie(movie_name)
        elif choice == "4":
            break
        else:
            print("Invalid. Try again.\n")


if __name__ == "__main__":
    main()
