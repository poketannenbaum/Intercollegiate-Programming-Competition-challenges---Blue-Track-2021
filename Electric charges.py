usage = input("Enter the amount of hours used: ")
usage = int(usage)
charge = 0

if(usage <= 1000):
	charge = usage * 7.633
else:
	charge = usage * 9.259
dollars = charge / 100 
print (f"Your charge is: {charge} cents, or {dollars} dollars")