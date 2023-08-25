import tkinter as tk
from tkinter import messagebox
from datetime import datetime
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


def show_movie_details(event, listbox_movies, text_output, delete_button, root):
    selected_index = listbox_movies.curselection()

    if not selected_index:
        text_output.delete("1.0", tk.END)
        delete_button.pack_forget()
        return

    movie_name = listbox_movies.get(selected_index).split(" - ")[0]
    data = read_write_json()

    for movie in data["movies"]:
        if movie["Movie name"].lower() == movie_name.lower():
            formatted_output = (
                f"Movie name: {movie['Movie name']}\n"
                f"Genre: {', '.join(movie['Genre'])}\n"
                f"Runtime: {movie['Runtime']} seconds\n"
                f"Metascore: {movie['Metascore']}\n"
                f"IMDb rating: {movie['IMDb ratings']}\n"
                f"Lead actors: {', '.join(movie['Lead actors'])}\n"
                f"Release date: {get_formatted_datetime(movie['Release date'])}\n"
            )
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, formatted_output)

            delete_button.config(
                command=lambda: delete_movie(movie_name, text_output, delete_button, listbox_movies, root)
            )

            delete_button.pack()


def delete_movie(movie_name, text_output, delete_button, listbox_movies, root):
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
        display_movie_names_ratings(listbox_movies)
        text_output.delete("1.0", tk.END)
        delete_button.pack_forget()
    else:
        messagebox.showinfo("Error", "Movie not found.")


def main_gui():
    root = tk.Tk()
    root.title("Movie Management GUI")

    listbox_movies = tk.Listbox(root, height=15, width=60)
    listbox_movies.pack()

    add_button = tk.Button(root, text="Add Movie", command=add_movie_gui)
    add_button.pack()

    text_output = tk.Text(root, height=15, width=60)
    text_output.pack()

    delete_button = tk.Button(root, text="Delete Movie", command=lambda: None)

    listbox_movies.bind("<<ListboxSelect>>", lambda event: show_movie_details(
        event, listbox_movies, text_output, delete_button, root
    ))

    display_movie_names_ratings(listbox_movies)

    root.mainloop()


def add_movie_gui():
    btn_save = tk.Button


if __name__ == "__main__":
    main_gui()
