class Pulsar(object):
    """
    ATTRIBUTES
    x, y
    fuel



    isulation

    METHODS
    launch
    move
    explode

    """
    def __init__(self, vel_y):
        self.x = 0
        self.y = 0
        self.vel_x = 1
        self.vel_y = 1
        self.fuel = 100
        self.g = -.098

    def move(self):
        self.vel_y += self.g
        self.x += self.vel_x
        self.y += self.vel_y
        self.fuel -= 1
        self.status()
        if self.is_crashed():
            print ("YOU CRASHED")

    def status(self):
        print(f"The Pulsar is at {self.x}, {self.y}")
        print (f"Velocity: {self.vel_x}, {self.vel_y}")
        print (f"Fuel Remaining: {round(self.fuel,2)}%")
        print("---")

    def is_crashed(self):
        if self.y <= 0:
            return True
        else:
            return False



a = Pulsar(100)
#b = Pulsar()

a.x
a.move()
a.x
a.y
for x in range(1000):
    a.move()
    if a.is_crashed:
        break
    if x % 10 == 0:
        a.status()
a.x
