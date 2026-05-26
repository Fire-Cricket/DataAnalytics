# Jordan R. Worrobah
# 5/26/2026

class Restaurant():

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print("-----Restaurant-----")
        print(f"{self.rest_name} serves {self.food_type}.")
        print()

    def rest_open(self):
        print("-----Status-----")
        print(f"{self.rest_name} is open.")
        print()

    def add_num_served(self):
        while True:
            try:
                customers = int(input("How many customers served today? "))
                self.number_served += customers
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.\n")

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.\n")

    def customer_rating(self):
        while True:
            rating = input(
                "How would you rate your experience today on a scale of 1-5 "
                "(5 being excellent)? "
            )

            if rating.isdigit():
                rating = int(rating)

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}.")
                    print(f"The average rating for this restaurant is {average:.1f}\n")
                    break

            print("Invalid rating. Please enter a whole number from 1-5.\n")


restaurant1 = Restaurant('McDonalds', 'Burgers')
restaurant2 = Restaurant('Dairy Queen', 'Ice Cream')
restaurant3 = Restaurant('Chipotle', 'Tacos')


class FoodTruck(Restaurant):
    """Child class that represents a food truck version of a restaurant."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)

        self.private_bookings = 'N'
        self.truck_location = ""

        
        self.location_history = []

    def accepts_private_bookings(self):
        while True:
            booking = input(
                "Does this food truck accept private bookings? Y/N "
            ).upper()

            if booking == "Y" or booking == "N":
                self.private_bookings = booking
                break

            print("Invalid input. Please enter Y or N.\n")

        if self.private_bookings == "Y":
            print("This food truck currently accepts private bookings.\n")
        else:
            print("This food truck currently does not accept private bookings.\n")

    def relocate_truck(self):
        self.truck_location = input(
            "Enter the truck's current location, street address and city: "
        )

        self.location_history.append(self.truck_location)

        print(f"Truck is currently located at {self.truck_location}\n")

    def print_location_history(self):
        print("-----Location History-----")

        for location in self.location_history:
            print(location)

        print()


food_truck1 = FoodTruck("Jordan's River Grill", "Chicken and Rice")

food_truck1.describe_rest()
food_truck1.rest_open()

food_truck1.accepts_private_bookings()

food_truck1.relocate_truck()
food_truck1.relocate_truck()
food_truck1.relocate_truck()

food_truck1.print_location_history()