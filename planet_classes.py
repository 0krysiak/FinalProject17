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
    Population: {self.population}
    Description: {self.description}"""

mercury = Planet("Mercury", 657, 0, "No", 0, """Mercury is in danger of falling into the sun, which is why it is not inhabited.
                 The slighest force could cause Mercury to fall out of orbit and right into the Sun""") #If player chooses Mercury, they die

venus = Planet("Venus", 801, 0, "Yes", "approx. 2 billion", """Venus is one of the hottest planets, along with Mercury and Earth. Because of
             this, the Venus population are creaturs with extremely thick skin and low body temperatures.
             They live underground, where the air is cooler,
             so the planet seems empty upon first arrival.""")

earth = Planet("Earth", 900, 1, "No", 0, """Earth looks totally different from the Earth you came from. There are erupting volcanos, earthquakes,
                tsunamis. Conditions are too dangerous to house any human-like creatures.""")

mars = Planet("Mars", 70, 2, "Yes", "approx. 1 billion", """Mars is the only planet that has human-like creatures living on it. Since Mars
              has conditions close to Earth's (the one you came from), Mars is relatively harmless. There is no way to predict how Mars's inhabitants
              will react if someone or something were to land on their planet""")

jupiter = Planet("Jupiter",235, 67, "Yes", 3, """Jupiter is home to the only 3 Wind Wyverns in the universe.
                 They scour the planet and protect whatever they may be hiding in the center of Jupiter.
                 They are extremely smart, quick, and dangerous""")

saturn = Planet("Saturn", -288, 62, "Yes", "approx. 300 billion", """Saturn's inhabitants are hostile and do not like things
                coming from other planets. They never leave or allow anyone on their planet. Because of the
                highly pressurized liquid hydrogen and helium beneath the surface, towering geysers have been seen to
                shoot from the planet, killing any non-natives that come in contact with it.""")

uranus = Planet("Uranus", -357, 27, "No", 0, "No body wanted to live on Uranus")

neptune = Planet("Neptune", -200, 2, "no", 0, """Neptune's atmosphere is mainly methane, and its interior is methane ice.
                Between this and the extreme cold, no creature has been able to adapt to both of these environments at once""")

pluto = Planet("Pluto", -380, 5, "Yes", "approx. 100,000", """Pluto is the smallest planet and contains the most peaceful inhabitants.
                They are small creatures that keep to themselves and will not bother you as long as you don't bother them. Not many
                other creatures visit Pluto because of its extreme cold""")

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto ]

current_planet = planets[5]

#print(f"Mercury's temperature is {current_planet.temperature}")
print(current_planet)