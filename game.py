# import sys

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
    blackhole_= input("You just wasted a month of your life")
print("Flying into V616 Mon!")
# Allows player to choose if they would like to move on or not

print("""As you enter the black hole, you feel extreme turbulence. All of the controls are going crazy and there are noises and bright lights everywhere.
After a few terrifying minutes, it all suddenly stops.


What do you do first?:
    1. Check Fuel
    2. Call Ground Control
    3. Eject Yourself from Space Ship""")

one = 'check_fuel'
two = 'call'
three = 'eject'

choice = input("Type the number 1, 2, or 3 to choose your path: ")
if choice == one:
    print("There is no fuel left. How are you still flying?")
elif choice == two:
    print("You are unable to call Ground Control, no signal is getting through.")
else:
    print("No one will ever know what was in that black hole")





