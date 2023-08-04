import json
file_path = "movies.json"

with open(file_path, "r") as json_file:
    data = json.load(json_file)

movies_list = data["movies"]

formatted_output = ""
for movie in movies_list:
    formatted_output += f"Movie name is {movie['Movie name']}. Its genre is {', '.join(movie['Genre'])}. "
    formatted_output += f"The runtime of the movie is {movie['Runtime']} seconds. The Metascore for the movie is {movie['Metascore']}. "
    formatted_output += f"The IMDb rating is {movie['IMDb ratings']}. The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
    formatted_output += f"The release date of the movie is {movie['Release date']} (Unix timestamp).\n\n"

print(formatted_output)
