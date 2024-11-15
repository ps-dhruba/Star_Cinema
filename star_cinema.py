class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.seats = {}
        self.show_list = [] 
        self.entry_hall(self)

    def entry_show(self,show_id,movie_name,time):
        show_info = (show_id,movie_name,time)
        self.show_list.append(show_info) 
        seat_layout = [ ["Free  " for j in range(self.__cols) ] for i in range(self.__rows) ]
        self.seats[show_id] = seat_layout

    def book_seats(self, show_id, seat_positions):
        if show_id not in self.seats:
            print(f"{show_id} is an invalid show id.")
            return
        seat_layout = self.seats[show_id]


        for row,col in seat_positions:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Seat at row {row+1}, column {col+1} is out of range.")
            elif seat_layout[row][col] == "Free  ":
                seat_layout[row][col] = "Booked"
                print(f"Seat at row {row+1}, column {col+1} booked successfully.")
            else:
                print(f"Sorry! Seat at row {row+1}, column {col+1} is already booked.")

    def view_show_list(self):
        for show in self.show_list:
            show_id, movie_name, time = show
            print(f"Show ID: {show_id} ---- Movie: {movie_name} ---- Date: 9/11/2024 ---- Time: {time}")

    def view_available_seats(self,show_id):
        if show_id not in self.seats:
            print(f"{show_id} is an invalid show id.")
            return
        seat_layout = self.seats[show_id]

        print(f"\nSeat configuration for show {show_id}:\n")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(seat_layout[i][j], end = " ")
            print()

def options():
    print("\n1.View all show today.")
    print("2.View available seats.")
    print("3.Book ticket.")
    print("4.Exit.")

hall1 = Hall(10,10,110)


hall1.entry_show("110","Spider Man","3:00 PM")
hall1.entry_show("111","Batman","6:00 PM")
hall1.entry_show("112","Forrest Gump","9:00 PM")

while True:
    options()
    choice = int(input("Enter option: "))

    if choice == 1:
        print("----------------------------------------------")
        hall1.view_show_list()
        print("----------------------------------------------")
    elif choice == 2:
        show_id = input("Enter show id: ")
        hall1.view_available_seats(show_id)
        print("----------------------------------------------")
    elif choice == 3:
        show_id = input("Enter show id: ")
        tickets = int(input("How many tickets do you want: "))

        seat_positions = []
        for i in range(tickets):
            row = int(input("Enter seat row [1,10]: "))
            col = int(input("Enter seat column [1,10]: "))
            seat_positions.append((row-1,col-1))

        print("\n----------------------------------------------")
        hall1.book_seats(show_id,seat_positions)
        print("----------------------------------------------")
    elif choice == 4:
        print("\nThanks for using the service. Have a good day!")
        break
    else:
        print("\nWrong option! Choose again")