class CAR:
  def __init__(self, colour,max_spd,accleration,tyre_frec,is_eng_started):
    self.colour = colour
    self.max_spd = max_spd
    self.accleration = accleration
    self.tyre_frec = tyre_frec
    self.is_eng_started = is_eng_started
    
car = CAR("Red","160 kmph","10kmph","5kmph","started")
x ="Car colour:"
print(x,car.colour)
x="Car Max_speed:"
print(x,car.max_spd)
x="Car Accleration:"
print(x,car.accleration)
x="car Tyre_frec:"
print(x,car.tyre_frec)
x="car is:"
print(x,car.is_eng_started)
