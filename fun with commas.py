wordlist = []
exitflag = ""
while (True):
	exitflag = input("Enter next word or quit:")
	if (exitflag == "quit"):
		break
	else:
		wordlist.append (exitflag)

arraylength = len(wordlist)
arraycounter = 0
while(arraylength > 1):
	print(f"{wordlist[arraycounter]},", end='')
	arraycounter = arraycounter + 1
	arraylength = arraylength - 1
if (arraylength == 1):
	print(f"and {wordlist[arraycounter]}")