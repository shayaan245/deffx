import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from movie_management import read_write_json

file_path = "movies.json"


def get_formatted_datetime(epoch_time):
    dt_object = datetime.fromtimestamp(epoch_time)
    formatted_datetime = dt_object.strftime("%d-%m-%Y")
    return formatted_datetime


def display_movies_gui(text_output):
    data = read_write_json()
    formatted_output_strings = [
        f"Movie name: {movie['Movie name']}\n"
        f"Genre: {', '.join(movie['Genre'])}\n"
        f"Runtime: {movie['Runtime']} seconds\n"
        f"Metascore: {movie['Metascore']}\n"
        f"IMDb rating: {movie['IMDb ratings']}\n"
        f"Lead actors: {', '.join(movie['Lead actors'])}\n"
        f"Release date: {get_formatted_datetime(movie['Release date'])}\n"
        for movie in data["movies"]
    ]
    formatted_output = "\n".join(formatted_output_strings)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, formatted_output)


def add_movie_gui(text_output, entry_movie_name, entry_genre, entry_runtime, entry_metascore, entry_imdb, entry_actors,
                  entry_release):
    movie_name = entry_movie_name.get()
    genre = entry_genre.get()
    runtime = entry_runtime.get()
    metascore = entry_metascore.get()
    imdb = entry_imdb.get()
    actors = entry_actors.get()
    release = entry_release.get()

    if not (movie_name and genre and runtime and metascore and imdb and actors and release):
        messagebox.showinfo("Error", "Please enter all movie details.")
        return

    movie = {
        "Movie name": movie_name,
        "Genre": genre.split(","),
        "Runtime": int(runtime),
        "Metascore": int(metascore),
        "IMDb ratings": float(imdb),
        "Lead actors": actors.split(","),
        "Release date": int(datetime.strptime(release, "%d-%m-%Y").timestamp())
    }

    data = read_write_json()
    movie_name_lower = movie_name.lower()
    movies_list = data["movies"]

    for existing_movie in movies_list:
        if existing_movie["Movie name"].lower() == movie_name_lower:
            messagebox.showinfo("Error", "Movie with the same name already exists.")
            return

    movies_list.append(movie)
    read_write_json(data, write=True)
    messagebox.showinfo("Success", "Movie added successfully!")
    display_movies_gui(text_output)

def delete_movie_gui(text_output, entry_movie_name):
    movie_name = entry_movie_name.get()
    data = read_write_json()
    movies_list = data["movies"]
    found = False

    for movie in movies_list:
        if movie["Movie name"].lower() == movie_name.lower():
            movies_list.remove(movie)
            found = True
            break

    if found:
        read_write_json(data, write=True)
        messagebox.showinfo("Success", "Movie deleted successfully!")
        display_movies_gui(text_output)
    else:
        messagebox.showinfo("Error", "Movie not found.")


def main_gui():
    root = tk.Tk()
    root.title("Movie Management GUI")

    btn_display_movies = tk.Button(root, text="Display Movies", command=lambda: display_movies_gui(text_output))
    btn_display_movies.pack()

    entry_movie_name = tk.Entry(root, width=30)
    entry_movie_name.pack()
    label_genre = tk.Label(root, text="Genre (comma-separated):")
    label_genre.pack()
    entry_genre = tk.Entry(root, width=30)
    entry_genre.pack()
    label_runtime = tk.Label(root, text="Runtime (seconds):")
    label_runtime.pack()
    entry_runtime = tk.Entry(root, width=30)
    entry_runtime.pack()
    label_metascore = tk.Label(root, text="Metascore:")
    label_metascore.pack()
    entry_metascore = tk.Entry(root, width=30)
    entry_metascore.pack()
    label_imdb = tk.Label(root, text="IMDb rating:")
    label_imdb.pack()
    entry_imdb = tk.Entry(root, width=30)
    entry_imdb.pack()
    label_actors = tk.Label(root, text="Lead actors (comma-separated):")
    label_actors.pack()
    entry_actors = tk.Entry(root, width=30)
    entry_actors.pack()
    label_release = tk.Label(root, text="Release date (DD-MM-YYYY):")
    label_release.pack()
    entry_release = tk.Entry(root, width=30)
    entry_release.pack()

    btn_add_movie = tk.Button(root, text="Add Movie", command=lambda: add_movie_gui(
        text_output, entry_movie_name, entry_genre, entry_runtime,
        entry_metascore, entry_imdb, entry_actors, entry_release
    ))
    btn_add_movie.pack()

    entry_delete_movie = tk.Entry(root, width=30)
    entry_delete_movie.pack()
    btn_delete_movie = tk.Button(root, text="Delete Movie",
                                 command=lambda: delete_movie_gui(text_output, entry_delete_movie))
    btn_delete_movie.pack()

    text_output = tk.Text(root, height=15, width=60)
    text_output.pack()

    root.mainloop()


if __name__ == "__main__":
    main_gui()
