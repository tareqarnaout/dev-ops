c = 0
while True:
    answer = input("Do you like Python? (enter y or n): ")
    if answer == 'y':
        break

    print("Are you " + 'really ' * c + "sure you don't like Python?")
    print("I will ask again:")
    c = c + 1

print("Thank you! I knew you loved Python!")