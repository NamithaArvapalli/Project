class Movie:
    def __init__(self, title, duration, available_seats):
        self.title = title
        self.duration = duration
        self.available_seats = available_seats

    def __str__(self):
        return f"{self.title} ({self.duration} mins)"


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        print("Available Movies:")
        for i, movie in enumerate(self.movies, 1):
            print(f"{i}. {movie}")

    def get_movie_by_index(self, index):
        if 0 < index <= len(self.movies):
            return self.movies[index - 1]
        else:
            return None


class SeatReservationSystem:
    def __init__(self):
        self.booked_seats = set()

    def book_seat(self, seat):
        self.booked_seats.add(seat)

    def is_seat_available(self, seat):
        return seat not in self.booked_seats


def main():
    cinema = Cinema()
    cinema.add_movie(Movie("Rebal", 175, 100))
    cinema.add_movie(Movie("Don", 142, 80))
    cinema.add_movie(Movie("Sye", 154, 120))

    seat_reservation = SeatReservationSystem()

    while True:
        print("\nWelcome to Movie Ticket Booking System")
        print("1. Show available movies")
        print("2. Book tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cinema.show_movies()
        elif choice == "2":
            movie_index = int(input("Enter the movie number to book tickets: "))
            movie = cinema.get_movie_by_index(movie_index)
            if movie:
                print(f"Selected movie: {movie.title}")
                num_tickets = int(input("Enter the number of tickets: "))
                available_seats = movie.available_seats
                if num_tickets <= available_seats:
                    for _ in range(num_tickets):
                        seat = input("Enter the seat number (e.g., A1): ").upper()
                        if seat_reservation.is_seat_available(seat):
                            seat_reservation.book_seat(seat)
                            print(f"Seat {seat} booked successfully!")
                        else:
                            print(f"Seat {seat} is already booked. Please choose another seat.")
                else:
                    print("Sorry, not enough seats available.")
            else:
                print("Invalid movie selection.")
        elif choice == "3":
            print("Thank you for using Movie Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
