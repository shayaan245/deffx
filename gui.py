import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
from movie_management import read_write_json

file_path = "movies.json"

def get_formatted_datetime(epoch_time):
    dt_object = datetime.fromtimestamp(epoch_time)
    formatted_datetime = dt_object.strftime("%d-%m-%Y")
    return formatted_datetime

def display_movie_names_ratings(listbox_movies):
    data = read_write_json()
    listbox_movies.delete(0, tk.END)

    for movie in data["movies"]:
        listbox_movies.insert(tk.END, f"{movie['Movie name']} - IMDb: {movie['IMDb ratings']}")

def create_movie_details_window(movie, listbox_movies):
    top = tk.Toplevel()
    top.title("Movie Details")
    hours, remainder = divmod(movie['Runtime'], 3600)
    minutes, _ = divmod(remainder, 60)

    formatted_runtime = f"{hours}h {minutes}m"

    formatted_output = (
        f"Movie name: {movie['Movie name']}\n"
        f"Genre: {', '.join(movie['Genre'])}\n"
        f"Runtime: {formatted_runtime}\n"
        f"Metascore: {movie['Metascore']}\n"
        f"IMDb rating: {movie['IMDb ratings']}\n"
        f"Lead actors: {', '.join(movie['Lead actors'])}\n"
        f"Release date: {get_formatted_datetime(movie['Release date'])}\n"
    )

    text_output = tk.Text(top, height=15, width=60)
    text_output.insert(tk.END, formatted_output)
    text_output.pack()

    delete_button = tk.Button(top, text="Delete Movie", command=lambda: delete_movie(movie, top, listbox_movies))
    delete_button.pack()

    close_button = tk.Button(top, text="Close", command=top.destroy)
    close_button.pack()

def delete_movie(movie, top, listbox_movies):
    confirmed = messagebox.askyesno("Confirmation", f"Do you want to delete the movie '{movie['Movie name']}'?")

    if confirmed:
        data = read_write_json()
        movies_list = data["movies"]
        found = False

        for movie_item in movies_list:
            if movie_item["Movie name"].lower() == movie["Movie name"].lower():
                movies_list.remove(movie_item)
                found = True
                break

        if found:
            read_write_json(data, write=True)
            messagebox.showinfo("Success", "Movie deleted successfully!")
            top.destroy()
            display_movie_names_ratings(listbox_movies)  # Refresh the list
        else:
            messagebox.showinfo("Error", "Movie not found.")

def main_gui():
    root = tk.Tk()
    root.title("Movie Management GUI")

    listbox_movies = tk.Listbox(root, height=15, width=60)
    listbox_movies.pack()

    add_button = tk.Button(root, text="Add Movie", command=lambda: add_movie_gui(listbox_movies))
    add_button.pack()

    listbox_movies.bind("<Double-Button-1>", lambda event: show_movie_details(event, listbox_movies))

    display_movie_names_ratings(listbox_movies)

    root.mainloop()

def add_movie_gui(listbox_movies):
    top = tk.Toplevel()
    top.title("Add Movie")

    label_movie_name = tk.Label(top, text="Movie Name:")
    entry_movie_name = tk.Entry(top)
    label_genre = tk.Label(top, text="Genre (comma-separated):")
    entry_genre = tk.Entry(top)
    label_runtime = tk.Label(top, text="Runtime (HH:MM ):")
    entry_runtime = tk.Entry(top)
    label_metascore = tk.Label(top, text="Metascore:")
    entry_metascore = tk.Entry(top)
    label_imdb = tk.Label(top, text="IMDb rating:")
    entry_imdb = tk.Entry(top)
    label_actors = tk.Label(top, text="Lead actors (comma-separated):")
    entry_actors = tk.Entry(top)
    label_release = tk.Label(top, text="Release date (DD-MM-YYYY):")
    entry_release = tk.Entry(top)

    def validate_input():
        label_movie_name_error.config(text="")
        label_genre_error.config(text="")
        label_runtime_error.config(text="")
        label_metascore_error.config(text="")
        label_imdb_error.config(text="")
        label_actors_error.config(text="")
        label_release_error.config(text="")

        movie_name = entry_movie_name.get()
        genre = entry_genre.get()
        runtime = entry_runtime.get()
        metascore = entry_metascore.get()
        imdb = entry_imdb.get()
        actors = entry_actors.get()
        release = entry_release.get()

        if not movie_name:
            label_movie_name_error.config(text="Movie name is required.")
        if not genre:
            label_genre_error.config(text="Genre is required.")
        if not is_valid_runtime(runtime):
            label_runtime_error.config(text="Invalid runtime format. Use HH:MM .")
        if not imdb:
            label_imdb_error.config(text="IMDb rating is required.")
        elif not imdb.replace('.', '', 1).isdigit():
            label_imdb_error.config(text="IMDb rating must be a number.")
        if not metascore:
            label_metascore_error.config(text="Metascore is required.")
        elif not is_valid_metascore(metascore):
            label_metascore_error.config(text="Metascore must be a number.")
        if not actors:
            label_actors_error.config(text="Lead actors are required.")

        try:
            datetime.strptime(release, "%d-%m-%Y")
        except ValueError:
            label_release_error.config(text="Invalid release date format. Use DD-MM-YYYY")
            return False

        return True

    def is_valid_metascore(value):
        try:
            score = float(value)
            return 0 <= score <= 10
        except ValueError:
            return False

    def is_valid_runtime(value):
        try:
            time.strptime(value, "%H:%M")
            return True
        except ValueError:
            return False

    def save_movie(listbox_movies=None):
        if not validate_input():
            return

        movie_name = entry_movie_name.get()
        genre = entry_genre.get()
        runtime = entry_runtime.get()
        metascore = entry_metascore.get()
        imdb = entry_imdb.get()
        actors = entry_actors.get()
        release = entry_release.get()

        release = release.rstrip()

        # Split the runtime input to hours, minutes, and seconds (if present)
        runtime_parts = runtime.split(":")
        hours = int(runtime_parts[0])
        minutes = int(runtime_parts[1])

        total_seconds = (hours * 3600) + (minutes * 60)

        movie = {
            "Movie name": movie_name,
            "Genre": genre.split(","),
            "Runtime": total_seconds,
            "Metascore": float(metascore),
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
        top.destroy()
        display_movie_names_ratings(listbox_movies)

    label_movie_name.pack()
    entry_movie_name.pack()
    label_movie_name_error = tk.Label(top, text="", fg="red")
    label_movie_name_error.pack()

    label_genre.pack()
    entry_genre.pack()
    label_genre_error = tk.Label(top, text="", fg="red")
    label_genre_error.pack()

    label_runtime.pack()
    entry_runtime.pack()
    label_runtime_error = tk.Label(top, text="", fg="red")
    label_runtime_error.pack()

    label_metascore.pack()
    entry_metascore.pack()
    label_metascore_error = tk.Label(top, text="", fg="red")
    label_metascore_error.pack()

    label_imdb.pack()
    entry_imdb.pack()
    label_imdb_error = tk.Label(top, text="", fg="red")
    label_imdb_error.pack()

    label_actors.pack()
    entry_actors.pack()
    label_actors_error = tk.Label(top, text="", fg="red")
    label_actors_error.pack()

    label_release.pack()
    entry_release.pack()
    label_release_error = tk.Label(top, text="", fg="red")
    label_release_error.pack()

    btn_save = tk.Button(top, text="Save Movie", command=lambda: save_movie(listbox_movies))
    btn_save.pack()

    top.mainloop()

def show_movie_details(event, listbox_movies):
    selected_index = listbox_movies.curselection()

    if not selected_index:
        return

    movie_name = listbox_movies.get(selected_index).split(" - ")[0]
    data = read_write_json()

    for movie in data["movies"]:
        if movie["Movie name"].lower() == movie_name.lower():
            create_movie_details_window(movie, listbox_movies)
            break

if __name__ == "__main__":
    main_gui()