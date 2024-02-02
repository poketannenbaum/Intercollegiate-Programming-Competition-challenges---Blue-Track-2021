import re
numberlist = input("Enter the desired sum, number of elements, each element: ")
numberarray = re.split(" ", numberlist)
numberarray = list(map(int, numberarray))
desiredsum = numberarray[0]
numberarray.pop(0)
numberarraysize = len(numberarray)
runningtally = 0
maincounter = 0
founddastuff = 0
internalcounter = 0
while (maincounter != len(numberarray)):
	currentnumber = numberarray[maincounter]
	internalcounter = maincounter
	for num in numberarray:
		if (internalcounter == len(numberarray) -1):
			break
		proceedingnumber = numberarray[internalcounter + 1]
		internalcounter = internalcounter + 1
		if (currentnumber + proceedingnumber == desiredsum):
			founddastuff = 1
			print(f"({currentnumber}, {proceedingnumber}) found at [{maincounter}],[{internalcounter}]")
			break
	maincounter = maincounter + 1
if (founddastuff == 0):
	print ("No pairs found")