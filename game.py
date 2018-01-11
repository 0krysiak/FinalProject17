print("""Welcome! You have been chosen to be the first person to use the new AquaMaster!
It’s the newest, state-of-the-art technology that will be used to explore the deep seas and its inhabitants.
You will begin your journey shortly. Good luck!""")

name = input("What is your name? ")
print(name)

start = 'yes'
start_ = input("Alright, it is time to start your journey! Are you ready? ")
if start_ == start:
    print("Let's go!")
else:
   print("Really? Okay, we'll get someone else to try the AquaMaster.")


answer = 'yes'
answer_ = input("To start off, would you like to see the status of the AquaMaster? ")
while answer_ != answer:
    answer_ = input("""Are you sure? There could be some important information.
    Answer again. """)
print(f"Okay. Here is the current status")

# ************make a class and put here************













