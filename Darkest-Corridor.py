__author__ = 'Raziel'

print("Welcome to the darkest corridor in the whole flipping world!")
print(" ")
print("As you near the entrance of the darkest corridor,")
print ("you see an old hunched over man.")
print("He beckons you near and speaks:")
print("What is your name Fell Warrior?")
name = input("> ")
print("Okay", name, "You may enter the corridor, but beware, beware!")

room = 1

while room != 7:
    if room == 1:
        print("You are at the beginning of the dark corridor.")
        print("It smells of still air and dank water.")
    elif room == 2:
        print("You are a little past the entrance of the dark corridor.")
        print("You think you might hear a low moaning deeper in the tunnel.")
    elif room == 3:
        print("You are in the center of the corridor.")
        print("There is definitely a painful moaning coming from somewhere.")
    elif room == 4:
        print("It's really dark, and somehting just ran past your foot.")
    elif room == 5:
        print("Thoughts of your own mortality accompany the sounds of")
        print("creaking, scuddling, moaning.")
    elif room == 6:
        print("You think you may see a little light.")
        print("Is the end of the corridor near?")

    print("What do you want to do", name,", go FORWARD, BACK, or stand and LOOK?")
    action = input("> ")
    if action == "FORWARD":
       room = room+1
    elif action == "BACK":
       room = room-1
    elif action == "LOOK":
       room = room
    else:
        print("You can't do that, or anything else for that matter --")
        print("you're just too terrified!")

print("You've escaped darkest corridor in the whole flipping world!")
print("THE END.")

