age = input("Enter your age: ")
yearsLeft = 90 - int(age)
daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12
# print("You have " + str(days) + " days left.")
print(f"You've {daysLeft} days , {int(weeksLeft)} weeks & {int(monthsLeft)} months left. ")
