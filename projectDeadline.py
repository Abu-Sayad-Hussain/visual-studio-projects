import datetime

#initiaize variables

strDeadLn = ""
nmbrOfDays = 0
nmbrOfWks = 0
nmbrOfrDays = 0

#Get today's date

currentDate = datetime.date.today()

#ask user to enter project deadline

strDeadLn = input("Enter project deadline (dd/mm/yyyy)")

deadLine = datetime.datetime.strptime(strDeadLn, "%d/%m/%Y").date()

#Calculaate difference between project deadline and today's date

nmbrOfDays = deadLine - currentDate

#Calculate number of week remaining

nmbrOfWks = nmbrOfDays.days / 7

#Calculate the remain days

nmbrOfrDays = nmbrOfDays.days % 7

#Print the value to the user

print("You have %d"  %nmbrOfWks + " weeks and %d"  %nmbrOfrDays + " days remaining to submit your project")