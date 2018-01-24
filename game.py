import sys
#print("your answer is", answer)

# print("""Welcome! You have been chosen to be the first person to test the Pulsar!
# It’s the newest, state-of-the-art technology that will be used to explore space and the universe in ways we have only before imagined.
# If you choose to accept your mission, you will taking a journey straight into the V616 Mon, the nearest black hole to our solar system.
# You will be the first person to ever enter a black hole, so keep in mind the risks""")
# # Welcoming screen

# name = input("What is your name? ")
# print(name)
# # Player inputs their name

# start = 'yes'
# response = input("Alright, it is time to start your journey! Are you ready? ").lower()
# if response in start:
#     print("""
#     Let's go!
# """)
# # If player says 'yes', they will proceed with the game

# else:
#     sys.exit(["Really? Okay, we'll get someone else to try the Pulsar."])
# # # Exits the player out of game. Must start over if they wish to play.


# answer = 'yes'
# answer_ = input("To start off, would you like to see the details of your mission? ").lower()
# while answer_ != answer:
#     answer_ = input("""Are you sure? There could be some important information.
#     Answer again. """)
# # If player enters anything except 'yes', they will be prompted again

# print(f"""Okay. Here are the details:

# Ship Name : The Pulsar
# Mission Statement : Take the Pulsar to the nearest black hole and explore the depths of V616 Mon.
# Duration of Trip : Approx One Month
# To Contact Ground Control: Press and Hold 'Ground Control' Button on Controls Table
# """)
# # # When player enters 'yes', the details of the mission will be displayed

# move_on_ok = 'ok'
# move_on= input("Type 'OK' To Move On ").lower()
# while move_on != move_on_ok:
#     move_on = input("Type 'OK' To Move On " ).lower()
# print(f"""
# ...

# You ride in the ship for a month, regularly contacting Ground Control, and everything is going as planned.

# Then...you see it.

#  Type 'Keep going' to enter the black hole.
# If you wish to stop here, type 'Turn around' """)
# # After this, player will be prompted to either keep going or to turn around

blackhole = 'keep going'
blackhole_ = input('Do you keep going or do you turn around? ').lower()
while blackhole_ != blackhole:
    blackhole_= input("You just wasted a month of your life").lower()
print("Flying into V616 Mon!")
# Allows player to choose if they would like to move on or not

print("""As you enter the black hole, you feel extreme turbulence.
All of the controls are going crazy and there are noises and bright lights everywhere.
After a few terrifying minutes, it all suddenly stops.


What do you do first?:
    1. Check Fuel
    2. Call Ground Control
    3. Eject Yourself from Space Ship""")
#Player is given three options to choose from in the next command

check_fuel = 'one'
call = 'two'
eject = 'three'

choice = input("Type the number 1, 2, or 3 to choose your path: ")
if choice == eject:
    sys.exit("No one will ever know what was in that black hole")
elif choice == check_fuel:
    print("There is no fuel left. How are you still flying?")
elif choice == call:
    print("You are unable to call Ground Control, no signal is getting through.")
# Player is able to choose which option they want to see played out

press_enter = 'enter'
enter_press = input("Type 'ENTER' to continue: ").lower()
while enter_press == press_enter:
    print("""

    No connection to Earth and you are still moving through space even with no fuel.
    Could this be...an alternate universe?!


    As you move through space you begin to see all the planets of the Solar System. They look normal except for one thing:
    Some look like they contain life.""")
    break

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


#planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto ]
planets_dict = {"Mercury": mercury, "Venus": venus, "Earth": earth, "Mars": mars, "Jupiter": jupiter, "Saturn": saturn, "Uranus": uranus, "Neptune": neptune, "Pluto": pluto}
visit = input("Which planet would you like to visit? ")
if visit in planets_dict:
    current_planet = planets_dict[visit]
    print(current_planet)





#print(f"Mercury's temperature is {current_planet.temperature}")
#print(current_planet)







