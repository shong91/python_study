# function
# method: class 안에 있는 function

class Car():
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black") # 값이 없다면 default = black
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

    def start(self):
        print(self) # self.__str__
        print(self.color)
        print("I started")
    
    
# Extending Class
class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)
        
    def __str__(self):
        return f"Car with no roof"

    def take_off(self):
        return "taking off"


# print(Car)  # nothing printed
# print(dir(Car))

porche = Convertible(color="green", price="$40")
# porche.color = "red"
# porche.start()
# print(porche) # porche.__str__
print(porche.color, porche.price)
print(porche.take_off())
print(porche)

ferrari = Car()
ferrari.color = "blue"
print(ferrari.color, ferrari.price)

mini = Car()
print(mini.color, mini.price)

