import re
numberlist = input("Enter count, integers separated by a space: ")
numberarray = re.split(" ", numberlist)
numberarray = list(map(int, numberarray))
numberarraysize = len(numberarray)
runningtally = 0
maincounter = 0
internalcounter = 0
while (maincounter != len(numberarray)):
	currentnumber = numberarray[maincounter]
	internalcounter = maincounter
	for num in numberarray:
		if (internalcounter == len(numberarray) -1):
			break
		proceedingnumber = numberarray[internalcounter + 1]
		internalcounter = internalcounter + 1
		if (currentnumber > proceedingnumber):
			runningtally += 1
			break
	maincounter = maincounter + 1
print(runningtally)