# intializing the variable
amount = 0

# ask the user to enter the amount of total purchase
strAmount = input("Enter the amount of your purchase: ")

# converting string value to float vaue
amount = float(strAmount)

# shipping condition whether extra cost needed or not
if amount < 50 :
    addAmount = amount + 10
    print("Including shipping charge you have to pay $%.2f" %addAmount)

else :
    print("You don't have to pay shipping charges. You have to pay $%.2f" %amount)