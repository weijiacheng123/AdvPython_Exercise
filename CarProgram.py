import Car as c

def main():
    car_make = input("what's the make of the car?\n")
    car_model = input("what's the car's year model?\n")
    car_speed = input("what's your speed now?\n")

    my_car = c.car(car_model,car_make,car_speed)
    #print(my_new_car.get_descriptive_name())
    print(my_car.get_descriptive_name())
    
    for accelerate in range(1,6):
        my_car.car_accelerate(5)
        my_car.get_speed(car_speed)
        print(c.car_accelerate)
        
    for brake in range(1,6):
        my_car.car_brake(5)
        my_car.get_speed(car_speed)
        print(c.car_brake)


main()
# creates a Car object then calls the accelerate method five times. After each call to the accelerate method, 
# get the current speed of the car and display it. 

# Then call the brake method five times. After each call to the brake method,
# get the current speed of the car and display it.