# Task 1 ==> Code Correction
attendees = float(input("Enter number of attendees: "))
venue = "large hall" if attendees >= 100 else "conference room"
print(venue)



# Task 2 ==> Venue Selection
attendees = float(input("Enter number of attendees: "))
venue = "large hall" if attendees >= 100 else "conference room"
if attendees > 200:
    equipment = 'audio system and projector'
elif attendees > 100:
    equipment = 'audio system'
else:
    equipment = 'no additional equipment'

print(f"Venue: {venue}")
print(f"Reccommended equipment: {equipment}")




# Task 3 ==> Catering Choices
catering_choice = input("Would you like vegitarian food?: ")
if catering_choice == 'Yes':
    print('We recommend the Veggie Delight Cateres')
else:
    print('Are other option is the Gourmet Meals Caterer')