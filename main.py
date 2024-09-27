x = int(input("Enter attendence :"))

if x>74:
    print("You're eligible.")
else:
    y = int(input("Do you have medical conditions? Enter 1 if yes and 2 if no : "))
    if y == 1:
        print("You're eligible.")
    else:
        print("You're not eligible.")