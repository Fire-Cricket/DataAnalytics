# Jordan R. Worrobah
# 5/22/2026

class Restaurant():
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    count = 0
    
    def describe_rest(self):
        print("-----Resturant-----")
        print(f"{self.rest_name} serves {self.food_type}.")
        print()

    def rest_open(self):
        print("-----Status-----")
        print(f"{self.rest_name} is open.")
        print()


restaurant1 = Restaurant('McDonalds', 'Burgers')
restaurant2 = Restaurant('Dairy Queen', 'Ice Cream')
restaurant3 = Restaurant('Chipotle', 'Tacos')

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()