class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This cas has {self.odometer_reading} mileos on it.")

my_new_car = car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
'''
# change odometer directly
my_new_car.odometer_reading = 23
'''
my_new_car.read_odometer()


