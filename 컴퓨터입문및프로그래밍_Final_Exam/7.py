#7

class Restaurant():
    def __init__ (self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        return "{} serves wonderful {}." .format(self.restaurant_name, self.cuisine_type)
    def open_restaurant(self):
        return "레스토랑이 오픈하였습니다."

a= Restaurant("The Mean Queen", "pizza")
b= Restaurant("Ludvig'S Bistro", "seafood")
c= Restaurant("Mango Thai", "thai food")

print(a.describe_restaurant())
print(b.describe_restaurant())
print(c.describe_restaurant())
