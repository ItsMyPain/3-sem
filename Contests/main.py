class Car:
    def __init__(self, cap, sp, nm):
        self.capacity = cap
        self.speed = sp
        self.number = nm


class RaceCar(Car):
    def __init__(self, sp):
        super().__init__(0, sp, None)



c = Car(1000, 100, "a720po")
print(c.capacity, c.speed, c.number)
r = RaceCar(300)
print(r.capacity, r.speed, r.number)

