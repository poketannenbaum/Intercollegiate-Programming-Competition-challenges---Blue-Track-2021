import re
position = input("enter X and Y separated by a space: ")
intposition = re.split(" ", position)
intposition[0] = int(intposition[0])
intposition[1] = int(intposition[1])
quadrant = ""
if (intposition[1] < 0 and intposition [0] < 0):
	quadrant = "Q3"
if (intposition[1] < 0 and intposition [0] > 0):
	quadrant = "Q4"
if (intposition[1] > 0 and intposition [0] > 0):
	quadrant = "Q1"
if (intposition[1] > 0 and intposition [0] < 0):
	quadrant = "Q2"
print(quadrant)