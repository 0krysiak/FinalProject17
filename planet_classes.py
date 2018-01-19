class Planet(object):
    """
    Attributes:

    Temperature: an integer representing the temperature of the suface of the planet
    Moons : an integer representing the number of moons a planet has
    Inhabited? : Yes or No
    Population : an integer representing the amount of inhabitants
    """

def __init__(self, temperature, moons, inhabited, population):
    """Return a new Planet object"""
    self.temperture = temperature
    self.moons = moons
    self.inhabited = inhabited
    self.population = population

# def inhabited(self):
#    """Is the planet inhabited or not?"""
#    if self.population is not None:
#        print("Yes")
#    if self.population is None:
#        print("No")

class Mercury(Planet):
    def __init__(self, temperature, moons, inhabited, population):
        self.temperature = temperature
        self.moons = moons
        self.inhabited = inhabited
        self.population = population










