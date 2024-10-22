# Task 1 ==> Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")


# Task 2 ==> Setting the Scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    cave_action = input('light a torch or proceed in the dark?')
    if cave_action == 'light a torch':
        print('You can now see. Explore the cave!')
    elif cave_action == 'proceed in the dark':
        print("Watch your step!")
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")    
#This one kicked my butt. I was trying to put all of the original variables above and it was driving me crazy lol.


#Task 3 ==> Default Path
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    cave_action = input('light a torch or proceed in the dark?')
    if cave_action == 'light a torch':
        print('You can now see. Explore the cave!')
    elif cave_action == 'proceed in the dark':
        print("Watch your step!")
    else:
        pass
else:
    pass