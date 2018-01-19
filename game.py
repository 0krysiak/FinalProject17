import sys

print("""Welcome! You have been chosen to be the first person to test the Pulsar!
It’s the newest, state-of-the-art technology that will be used to explore space and the universe in ways we have only before imagined.
If you choose to accept your mission, you will taking a journey straight into the V616 Mon, the nearest black hole to our solar system.
You will be the first person to ever enter a black hole, so keep in mind the risks""")

name = input("What is your name? ")
print(name)

start = 'yes'
response = input("Alright, it is time to start your journey! Are you ready? ").lower()
if response in start:
    print("""
    Let's go!
""")
else:
    sys.exit(["Really? Okay, we'll get someone else to try the Pulsar."])
# Exits the player out of game. Must start over if they wish to play.


answer = 'yes'
answer_ = input("To start off, would you like to see the status of the Pulsar? ").lower()
while answer_ != answer:
    answer_ = input("""Are you sure? There could be some important information.
    Answer again. """)
print(f"Okay. Here is the current status")

# ************make a class and put here************

#           ****Is there something the player could type at any time to get the status of the ship?

print("""There is enough fuel for the journey there and back.
It should only take 5 days to get to the edge of the black hole.""")















