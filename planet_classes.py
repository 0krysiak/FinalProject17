class Planet(object):
    """
    Attributes:
    Temperature: an integer representing the temperature of the suface of the planet
    Moons : an integer representing the number of moons a planet has
    Inhabited? : Yes or No
    Population : an integer representing the amount of inhabitants

    """

    def __init__(self, name, temperature, moons, inhabited, population):
        """Return a new Planet object"""
        self.name = name
        self.temperature = temperature
        self.moons = moons
        self.inhabited = inhabited
        self.population = population

    def __str__(self):
        return f""""{self.name} Status :
    Temperature: {self.temperature} degrees Fahrenheit
    Number of Moons : {self.moons}
    Is it Inhabited? : {self.inhabited}
    Population: {self.population}"""

mercury = Planet("Mercury", 100, 3, "yes", 300)
neptune = Planet("Neptune", -200, 2, "no", 0)
# mercury = Planet("Mercury")

planets = [mercury, neptune]

current_planet = planets[0]

#print(f"Mercury's temperature is {current_planet.temperature}")
print(mercury)