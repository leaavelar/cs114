print("Type in the amount of change to dispense in cents that is below 100?")
amount_total = int(input())
amount_quarter = amount_total // 25
num_total = amount_total - (amount_quarter + 25)
amount_dime = amount_total // 10
num_total = amount_total - (amount_dime + 10)
amount_nickles = amount_total // 5
num_total = amount_total - (amount_nickles + 5)
amount_penny = amount_total // 1
num_total = amount_total - (amount_penny + 1)
print("Quarters" , amount_quarter)
print("Dimes" , amount_dime)
print ("Nickles" , amount_nickles)
print("Pennies" , amount_penny)
