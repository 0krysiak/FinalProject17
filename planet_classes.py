class Planet(object):
    """
    Attributes:
    Temperature: an integer representing the temperature of the suface of the planet
    Moons : an integer representing the number of moons a planet has
    Inhabited? : Yes or No
    Population : an integer representing the amount of inhabitants

    """

    def __init__(self, name, temperature, moons, inhabited, population, description):
        """Return a new Planet object"""
        self.name = name
        self.temperature = temperature
        self.moons = moons
        self.inhabited = inhabited
        self.population = population
        self.description = description

    def __str__(self):
        return f"""{self.name} Status :
    Current Temperature: {self.temperature} degrees Fahrenheit
    Number of Moons : {self.moons}
    Is it Inhabited? : {self.inhabited}
    Population: {self.population}"""

mercury = Planet("Mercury", 657, 0, "No", 0)
venus = Planet("Venus", 801, 0, "Yes", "approx. 2 billion")
earth = Planet("Earth", 900, 1, "No", 0)
mars = Planet("Mars", 70, 2, "Yes", "approx. 1 billion")
jupiter = Planet("Jupiter",235, 67, "Yes", 3)
saturn = Planet("Saturn", -288, 62, "Yes", "approx. 300 billion")
uranus = Planet("Uranus", -357, 27, "No", 0)
neptune = Planet("Neptune", -200, 2, "no", 0)
pluto = Planet("Pluto", -380, 5, "Yes", "approx. 100,000")

planets = [mercury,venus, earth, mars, jupiter, saturn, uranus, neptune, pluto ]

current_planet = planets[4]

#print(f"Mercury's temperature is {current_planet.temperature}")
print(current_planet)