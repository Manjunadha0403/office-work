class CAR:
  def __init__(self, colour,max_spd,accleration,tyre_frec,is_eng_started):
    self.colour = colour
    self.max_spd = max_spd
    self.accleration = accleration
    self.tyre_frec = tyre_frec
    self.is_eng_started = is_eng_started
  def my_cars(self):
    colour = self.colour
    print(f"Hello user {colour} car is ready  if want start the car enter 1 or stop the car enter 0")
    Start = int(input("Enter The value 0/1:"))
    if Start == 1:
       y ="The Car is"
       print(y,car.is_eng_started)
    else:
       y="THe Car is stop or not"
       print(y,car.is_eng_started)
car = CAR("Red","160 kmph","10kmph","5kmph","Started")
car.my_cars()