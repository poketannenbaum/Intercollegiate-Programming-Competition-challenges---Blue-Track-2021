import re
numbers = input("Enter integers separated by a space.\nEnd with 0:")
separatenumbers = re.split(" ", numbers)
separatenumbers.pop()
arraycounter = len(separatenumbers) - 1
while (arraycounter >= 0):
	separatenumbers[arraycounter] = int(separatenumbers[arraycounter])
	arraycounter = arraycounter - 1
smallestnumber = min(separatenumbers)
biggestnumber = max(separatenumbers)
largestquotient = biggestnumber/smallestnumber
print(largestquotient)
