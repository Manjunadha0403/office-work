class CAR:
    def __init__(self, colour: str,max_spd: int,acceleration,tyre_frec,is_eng_started):
        self.colour = colour
        self.max_spd = max_spd
        self.acceleration = acceleration
        self.tyre_frec = tyre_frec
        self.is_eng_started = is_eng_started
        self.current_speed =0    
    def car_start(self):
        colour = self.colour
        self.is_eng_started = True
        print(f"Hello user Your {colour} car is started ")
    def car_stop(self):
        colour = self.colour
        self.is_eng_started = False
        print(f"Hello user Your {colour} car is not startedc")
car = CAR("Red",160,10,5,"Started")
car.car_start()
car.car_stop()
print(car.is_eng_started)
car.car_start()
print(car.is_eng_started)