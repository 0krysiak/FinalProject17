import sys




# def switch_planet(choose):
#     # Allows player to switch to a different planet
#     user_input = 'switch planets'
#     respond = input("Switch planets?")
#     if respond == user_input:
#         print(current_planet)

#print("your answer is", answer)

print(""">>>Welcome! You have been chosen to be the first person to test the Pulsar!
It’s the newest, state-of-the-art technology that will be used to explore space and the universe in ways we have only before imagined.
If you choose to accept your mission, you will taking a journey straight into the V616 Mon, the nearest black hole to our solar system.
You will be the first person to ever enter a black hole, so keep in mind the risks.""")
# Welcoming screen

name = input("What is your name? ")
print(name)
# Player inputs their name

start = 'yes'
response = input(">>>Alright, {name}, it is time to start your journey! Are you ready? ".format(name=name)).lower()
if response in start:
    print("""
    Let's go!
""")
# If player says 'yes', they will proceed with the game

else:
    sys.exit(["Really? Okay, we'll get someone else to try the Pulsar."])
# # Exits the player out of game. Must start over if they wish to play.


answer = 'yes'
answer_ = input(""">>>To start off, would you like to see the details of your mission?
""").lower()
while answer_ != answer:
    answer_ = input("""Are you sure? There could be some important information.
    Answer again. """)
# If player enters anything except 'yes', they will be prompted again

print(f""">>>Okay. Here are the details:

Ship Name : The Pulsar
Mission Statement : Take the Pulsar to the nearest black hole and explore the depths of V616 Mon.
Duration of Trip : Approx One Month (?)
If You Want to Visit Another Planet : __insert here__
""")
# # When player enters 'yes', the details of the mission will be displayed

move_on_ok = 'ok'
move_on= input("Type 'OK' To Move On ").lower()
while move_on != move_on_ok:
     move_on = input("Type 'OK' To Move On " ).lower()
print(f"""

>>>Time flies as you get ready for your mission. You are excited, extremely nervous, and even proud in yourself for taking on this risk

The day you are scheduled to take off, you say good bye to friends and family, board the ship and you're off!

""")

move_on_ok = 'ok'
move_on= input("Type 'OK' To Move On ").lower()
while move_on != move_on_ok:
    move_on = input("Type 'OK' To Move On " ).lower()
print(f"""


>>>You ride in the ship for a month, regularly contacting Ground Control, and everything is going as planned.

Then...you see it.

""")
# After this, player will be prompted to either keep going or to turn around

groundcontrol = 'ground control'
ground_control = input("Type 'Ground Control' to let them know you're about to enter the black hole ").lower()
while ground_control != groundcontrol:
    ground_control = input(" Didn't want to call Ground Control? Well, they called you. You better pick up (type 'Ground Control' to answer) ").lower()
print("""
_______________________________________________

Ground Control: Abort mission! Abort mission!
_______________________________________________
""")

blackhole = 'keep going'
blackhole_ = input(""">>>Now what? Do you keep going or do you turn around?

 Type 'Keep going' to enter the black hole.
If you wish to stop here, type 'Turn around' """).lower()
while blackhole_ != blackhole:
    blackhole_= input("You just wasted a month of your life").lower()
print("""
>>>Flying into V616 Mon!

""")
# Allows player to choose if they would like to move on or not

print(""">>>As you enter the black hole, you feel extreme turbulence.
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

choice = input("Type the number one, two, or three to choose your path: ")
if choice == eject:
    sys.exit("""
No one will ever know what was in that black hole""")
elif choice == check_fuel:
    print("""
There is no fuel left. How are you still flying?""")
elif choice == call:
    print("""
You are unable to call Ground Control, no signal is getting through.""")
# Player is able to choose which option they want to see played out

press_enter = 'enter'
enter_press = input("Type 'ENTER' to continue: ").lower()
while enter_press == press_enter:
    print("""

>>> No connection to Earth and you are still moving through space even with no fuel.
    Could this be...an alternate universe?!


    As you move through space you begin to see all the planets of the Solar System. They look normal except for one thing:
    Some look like they contain life.
    """)
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
The slightest force could cause Mercury to fall out of orbit and right into the Sun""") #If player chooses Mercury, they die

venus = Planet("Venus", 801, 0, "Yes", "approx. 2 billion", """Venus is one of the hottest planets, along with Mercury and Earth. Because of
this, the Venus population are creatures with extremely thick skin and are cold blooded.
They live underground, where the air is cooler,so the planet seems empty upon arrival.
""")

earth = Planet("Earth", 900, 1, "No", 0, """Earth looks totally different from the Earth you came from. There are erupting volcanoes, earthquakes,
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

uranus = Planet("Uranus", -357, 27, "No", 0, "???")

neptune = Planet("Neptune", -200, 2, "no", 0, """Neptune's atmosphere is mainly methane, and its interior is methane ice.
Between this and the extreme cold, no creature has been able to adapt to both of these environments at once""")

pluto = Planet("Pluto", -380, 5, "Yes", "approx. 100,000", """Pluto is the smallest planet and contains the most peaceful inhabitants.
They are small creatures that keep to themselves and will not bother you as long as you don't bother them. Not many
other creatures visit Pluto because of its extreme cold""")

planets_dict = {"Mercury": mercury, "Venus": venus, "Earth": earth, "Mars": mars, "Jupiter": jupiter, "Saturn": saturn, "Uranus": uranus, "Neptune": neptune, "Pluto": pluto}
visit = input("""Which planet would you like to visit?
Mercury
Venus
Earth
Mars
Jupiter
Saturn
Uranus
Neptune
Pluto
""")
# Player gets to choose which planet they would like to visit
if visit in planets_dict:
    current_planet = planets_dict[visit]
    print(current_planet)

# def change_current_planet(choose):
#     currentplanet = current_planet
#     if user_input == currentplanet:
#         print(current_planet)
#-------------------------------------------------------------------------------------------------------
if current_planet == mercury:
        sys.exit("""The force of the rocket ships's landing knocked Mercury out of orbit and it flew into the sun.

    You died""")
#Inputting Mercury to visit causes the death of the player and the game to exit
#-------------------------------------------------------------------------------------------------------
if current_planet == jupiter:
    print("""
    Be careful, these creatures are vicious.
    """)
# Player gets a warning message if the choose Jupiter

    fight_spaceray = 'space ray'
    fight_agility = 'agility'
    fight_spaceship = 'space ship'
    flee = 'run away'
    fight = input("""
One of the three monsters approaches you.
If you want to fight using a space ray, type 'space ray'
If you want to fight using your agility, type 'agility'
If you want to fight using your space ship, type 'space ship'
If you want to try to get away, type 'run away'
""")
    if fight == fight_spaceray:
        print("You shoot the monster in the eye with a space ray, temporaily blinding it. Get in your ship and run! ")
    elif fight == fight_agility:
        sys.exit("""You try to out run the monster, but between lack of gravity and the fact that this monster is 100 times your size, you can't do it.

    You died""")
    elif fight == fight_spaceship:
        print("""You hit the monster with your space ship, which effectivley knocks it out! But, now your space ship is ruined.

    All that's left to do is wait to see if the monster wakes back up...

    """)
    elif fight == flee:
        sys.exit("""You get away!

    Almost...

    The monster grabs your ship and crushes it in his fist.

    You died""")

#-------------------------------------------------------------------------------------------------------
if current_planet == pluto:
    print("""
    You become friends with the creatures that live on Pluto. They allow you to stay with them.
    """)
# If the player chooses Pluto, they are given this response
    stay = 'stay'
    leave = ['i want to go home', 'go home']
    stay_leave = input("Do you [stay] or do you want to [go home]?: ")
    if stay_leave == stay:
        print("And you live happily ever after on the icy dwarf planet that is Pluto!")
    if stay_leave in leave:
        print("""

    You take board your ship and leave the creatures of Pluto. Who knows if you make it back home...""")

# The player can choose whether to stay or leave Pluto

# #-------------------------------------------------------------------------------------------------------
if current_planet == uranus:
    print("???")
# #--------------------------------------------------------------------------------------------------------------
if current_planet == venus:
    print("""
    You see a landing strip that leads toward the center of the planet.""")

    surface = 'land on surface'
    landing = 'use landing strip'
    land = input("""Would you like to use use the landing strip or would you like to land on the surface?

    Type [land on surface] to land on the surface of Venus
    Type [use landing strip] to use the landing strip to land
    """)
    if land == surface:
            sys.exit("""The surface of Venus melts your ship!

        You died""")
    elif land == landing:
        print(""" You land inside a hallowed out area of underground Venus. All around you are creatures
        looking curiously at your ship. You can:
        [stay seated] in your ship and see what happens
        [leave] your ship and communicate with these creatures
        [fly] away in your ship and never go back
        """)

    stay_seated = 'stay seated'
    leave_ = 'leave'
    fly_away = 'fly'
    action = input("What would you like to do? ")
    if action ==  stay_seated:
        sys.exit("""The creatures don't like that. They begin to trash your ship!
         Your ship is ruined and you get attacked by them

         You died""")
    elif action == leave_:
        print("""You leave your ship and see these gruesome looking creatures up close and personal. They speak
        to each other in a language you can't understand.
        Next thing you know, you're being grabbed and pulled away into the depths of Venus.
        You wonder in fear what's in store for you...
        """)
    elif action == fly_away:
        print("""You start up the ship and blast out of there!
         You hear the creatures begin to scream and they follow you out of Venus with their own space ship!
         And thus begins a high speed chase through space.
         You should go to another planet, they won't land with you since they know they are not equipped to handle any other climate other than their own
         """)

#-------------------------------------------------------------------------------------------------------------------------------------
if current_planet == earth:
    print("""
    This looks totally different from your Earth. Maybe you shouldn't land here.
    """)
    another_planet = 'go to another planet'
    another = input("Type [go to another planet] to choose somewhere else to go. ")
    if another == another_planet:
        print("Which planet do you want to visit now? ")
    while another != another_planet:
        print("You should really go somewhere else if you want to live")
        break #put function here that calls back planets list to choose from

#-------------------------------------------------------------------------------------------------------------------------------------
if current_planet == neptune:
    print("The climate on Neptune is extremely cold. Landing on this planet may be dangerous")
    land_neptune = 'yes'
    leave_neptune = 'no'
    neptune_landing = input("Are you sure you still want to land on Neptune? [yes] or [no] ")
    if neptune_landing == land_neptune:
        print("""As soon as you enter Neptune's atmosphere, your ship begins to freeze and you can feel the cold seeping into
        it. You need to get out as quickly as possible before you get stuff there.""")
    elif neptune_landing == leave_neptune:
        print("That was a good call")

#-------------------------------------------------------------------------------------------------------------------------------------
if current_planet == mars:
#Player can choose to explore Mars
    print(""" Landing on Mars makes you nervous for different reasons than if you were landing on another planet.
    It's so similar to Earth, even the creatures look like humans! They just seem much taller and...hairier
    """)
    action_explore = 'explore'
    action_talk = 'talk'
    action = input("""

Do you want to [explore] or [talk] to one of these creatures? """)
    if action == action_explore:
        print("""
        You find that Mars has many similarities to your Earth. There are some weird looking plants, the creatures all wear clothes that could
        be considered fashionable, there are even buildings that contain homes, shops, and restaraunts.
        The food doesn't look like anything humans on your Earth would eat and everything seems to be in a different, unrecognizable language.
        Talking to them might be difficult""")
    elif action == action_talk:
        print("""You attempt to communicate with a creature but it begins to yell in another language that you don't recognize.
        And you know a lot of languages.
        You guess that they called over others because they begin to surround you and urgently yell things at you.
        It might be wise of you to get out of there.""")
#-------------------------------------------------------------------------------------------------------------------------------------
if current_planet == saturn:
#Player can choose to explore Saturn
    print(" Saturn is extremely dangerous, are you sure you want to land here? ")
    action_leave = 'leave'
    action_land = 'land'
    action_flyaround = 'fly around'
    what_do = input("Would you like you [leave] and go to another planet, [land] on Saturn, or [fly around] Saturn? ")

    if what_do == action_leave:
        print("Good idea, now choose another planet to go to.")
    if what_do == action_land:
        print(" The creatures that live on Saturn capture you! You know they are very aggressive and hostile so you fear what they have in store for you...")
        sys.exit()
    elif what_do == action_flyaround:
        print("""Those geysers you read about hit your ship as you are flying around Saturn looking for the best place to land.
        You died""")
        sys.exit()
