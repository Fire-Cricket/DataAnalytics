# Jordan R. Worrobah
# 5/26/2026

class Restaurant():
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0 
        self.customer_ratings = []

    count = 0
    
    def describe_rest(self):
        print("-----Resturant-----")
        print(f"{self.rest_name} serves {self.food_type}.")
        print()

    def rest_open(self):
        print("-----Status-----")
        print(f"{self.rest_name} is open.")
        print()
    
    def add_num_served(self):
        self.number_served += int(input("How many customers served today? "))
        
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.\n")

    
    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")

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

restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.add_num_served()
restaurant1.print_num_served()
restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()
print("----------Next----------\n")

restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.add_num_served()
restaurant2.print_num_served()
restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()
print("----------Next----------\n")

restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()
print("----------Next----------\n")

