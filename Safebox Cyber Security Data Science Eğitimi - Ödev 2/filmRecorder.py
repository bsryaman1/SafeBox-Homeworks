class FilmRecorder:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_movie(self):
        movie_name = input("Movie name: ")
        movie_genre = input("Movie genre: ")

        with open(self.file_name, "a") as file:
            file.write(f"{movie_name},{movie_genre}\n")

        print("Movie saved.")

    def search_movie(self):
        movie_name = input("Enter movie name to search: ")

        with open(self.file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                saved_movie_name = data[0]

                if movie_name.lower() == saved_movie_name.lower():
                    print("Movie found.")
                    print("Movie details:")
                    print(f"Name: {saved_movie_name}")
                    print(f"Genre: {data[1]}")
                    return

        print("Movie not found.")

    def delete_movie(self):
        movie_name = input("Enter movie name to delete: ")

        file_changed = False

        with open(self.file_name, "r") as file:
            lines = file.readlines()

        with open(self.file_name, "w") as file:
            for line in lines:
                line = line.strip()
                if line:
                    data = line.split(",")
                    saved_movie_name = data[0].strip()

                    if movie_name.lower() == saved_movie_name.lower():
                        file_changed = True
                    else:
                        file.write(line + "\n")

        if file_changed:
            print("Movie deleted.")
        else:
            print("Movie not found.")

    def run(self):
        while True:
            print("Movie Recording Program")
            print("1. Save Movie")
            print("2. Search Movie")
            print("3. Delete Movie")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            # if-elif-else structure
            if choice == "1":
                self.save_movie()
            elif choice == "2":
                self.search_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Try again.")


FilmRecorder("movies.txt").run()
