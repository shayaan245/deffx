import json

 file_path = "movies.json"


 with open(file_path, "r") as json_file:
     data = json.load(json_file)

 movies_list = data["movies"]



 def add_movie():
     movie = {}
     movie["Movie name"] = input("Enter the movie name: ")
     genres = input("Enter genres: ").split(",")
     movie["Genre"] = [genre.strip() for genre in genres]
     movie["Runtime"] = int(input("Enter the runtime of the movie: "))
     movie["Metascore"] = int(input("Enter the Metascore for the movie: "))
     movie["IMDb ratings"] = float(input("Enter the IMDb rating for the movie: "))
     lead_actors = input("Enter lead actors are: ").split(",")
     movie["Lead actors"] = [actor.strip() for actor in lead_actors]
     movie["Release date"] = int(input("Enter the release date of the movie is: "))

     movies_list.append(movie)
     print("Movie added successfully!\n")

 def display_movies():
     formatted_output = ""
     for movie in movies_list:
         formatted_output += f"Movie name is {movie['Movie name']}. Its genre is {', '.join(movie['Genre'])}. "
         formatted_output += f"The runtime of the movie is {movie['Runtime']} seconds. The Metascore for the movie is {movie['Metascore']}. "
         formatted_output += f"The IMDb rating is {movie['IMDb ratings']}. The lead actors of the movie are {', '.join(movie['Lead actors'])}. "
         formatted_output += f"The release date of the movie is {movie['Release date']} .\n\n"
     print(formatted_output)

 while True:
     print("1. Display Movies")
     print("2. Add a new Movie")
     print("3. Exit")

     choice = input("Enter your choice (1/2/3): ")

     if choice == "1":
         display_movies()
     elif choice == "2":
         add_movie()
     elif choice == "3":

         data["movies"] = movies_list
         with open(file_path, "w") as json_file:
             json.dump(data, json_file, indent=4)
         break
     else:
         print("Invalid choice. Please try again.\n")
