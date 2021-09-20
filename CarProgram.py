import Car

def main():
    car_maker = input("what's your car maker?\n")
    car_model = input("what's your car model?\n")
    car_year = input("when was your car made?\n")

    my_new_car = Car.car(car_year,car_maker,car_model)
    #print(my_new_car.get_descriptive_name())
    print(my_new_car.get_descriptive_name())
    
main()
