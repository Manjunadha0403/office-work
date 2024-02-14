class CAR:
    def __init__(self, colour:str, max_spd:int, acceleration:float, tyre_frec:int, is_eng_started:bool):
        self.colour = colour
        self.max_spd = max_spd
        self.acceleration = acceleration
        self.tyre_frec = tyre_frec
        self.is_eng_started = is_eng_started
        self.current_speed = 0

    def car_start(self):
        
        if(self.is_eng_started):
            print("car is already in start mode")
        else:
            self.is_eng_started = True

    def car_stop(self):
        if(self.is_eng_started):
            self.is_eng_started=False
        else:
            print("car is already stop mode")
    def car_acceletarion(self): 
        if self.is_eng_started:
            carincr= self.current_speed+self.acceleration
            if  carincr > self.max_spd:
                self.current_speed==self.max_spd
                print(f"The car reached maximum speed{self.max_spd}  kmph")
            else:
                self.current_speed=carincr
                print(f"The car speed is increased to {self.current_speed} kmph")
        else:
            print("car is not started")

car = CAR("Blue",160,10,5,True,500)
car.car_start()
car.car_acceletarion()