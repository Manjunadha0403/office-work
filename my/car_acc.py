class Person:
  def __init__(self, colour,max_spd,acceleration,tyre_frec,is_eng_started):
    self.colour = colour
    self.max_spd = max_spd
    self.acceleration = acceleration
    self.tyre_frec = tyre_frec
    self.is_eng_started = is_eng_started
    
  def my_cars(self):
    colour = self.colour
    print(f"Hello user {colour} car is ready  if want start the car enter 1 or stop the car enter 0")
    Start = int(input("Enter The value 0/1:"))
    if Start == 1:
      car_state ="The Car is"
      print(car_state,car.is_eng_started)
      moment = self.my_function 
    else:
      car_state="THe Car is stop or not"
      print(car_state,car.is_eng_started)

  
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
car = Person("Red",160 ,10,5,"Started")
car.my_cars()
car.my_function()