class Person:
    def __init__(self, colour, max_spd, acceleration, tyre_frec, is_eng_started):
        self.colour = colour
        self.max_spd = max_spd
        self.acceleration = acceleration
        self.tyre_frec = tyre_frec
        self.is_eng_started = is_eng_started

    def my_cars(self):
        colour = self.colour
        print(f"Hello user, {colour} car is ready if want start the car enter 1 or stop the car enter 0.")
        start = int(input("Enter the car mode 0/1: "))
        if start == 1:
            car_mode = "The Car is"
            print(car_mode, self.is_eng_started)
        else:
            car_mode = "The Car is stop or not"
            print(car_mode, self.is_eng_started)

    def my_function_b(self):
        slow = self.tyre_frec
        speed = self.my_function()  # Call my_function to get the current speed
        slow_down = input("If you want to decrease car speed (Y/N): ").upper()
        if slow_down == 'Y':
            x = float(input("Enter brake value 1-32: "))
            car_slow = x * slow
            car_speed = speed - car_slow
            if car_slow < speed:
                print(f"The car speed is decreased from {speed} kmph to {car_speed} kmph")
            else:
                print(f"The car speed is {0} kmph")
        else:
            print(f"The car speed is {speed} kmph")

    def my_function(self):
        initial_speed = 0
        accelerator = self.acceleration
        print("Please give the acceleration values between 0-16 kmph:")
        increase = float(input("Enter accelerator value: "))
        speed = increase * accelerator
        max_speed = self.max_spd
        if speed < max_speed:
            print(f"The car speed is increased from {initial_speed} kmph to {speed} kmph")
        else:
            print(f"The car reached maximum speed {self.max_spd} kmph")

        return speed  # Return the calculated speed
# Instantiate the object before calling the method
car = Person("Red", 160, 10, 5, "Started")
car.my_cars()
car.my_function_b()