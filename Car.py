class car:
    def __init__(self,make,model,speed):
        self.__make = make
        self.__year_model = model
        self.__speed = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.__year_model} {self.__make}, and your speed is {self.__speed}."
        return long_name.title()

# accelerate - The accelerate method should add 5 to the speed data attribute each time it is called.
    def car_accelerate(self,accelerate):
        accelerate += self.__speed

# brake - The brake method should subtract 5 from the speed data attribute each time it is called.
    def car_brake(self,brake):
        brake -= self.__speed

#  get_speed - The get_speed method should return the current speed.
    def get_speed(self,speed):
        self.__speed = speed

    
        





