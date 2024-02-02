import re
numbers1 = input("Enter first set of data separated by space:")
numbers2 = input("Enter second set of data separated by space:")
array1 = re.split(" ", numbers1)
array2 = re.split(" ", numbers2)
array1int = list(map(int, array1))
array2int = list(map(int, array2))
masterarray = array1int + array2int
flagfornodiff = 0
array1int.sort()
array2int.sort()
array1len = len(array1int)
array2len = len(array2int)
counter = array1len - 1
masterarray.sort()
masterarraylength = len(masterarray)
result = []
i = 0
if (array1len == array2len):
	while (counter >= 0):
		if (array1int[counter] != array2int[counter]):
			break
		counter = counter - 1
	flagfornodiff = 1
result = []
while (masterarraylength > 0):
	if masterarray[i] not in result:
		result.append(masterarray[i])
	else:
		result.remove(masterarray[i])
	i = i + 1
	masterarraylength = masterarraylength - 1
if(flagfornodiff == 1):
	print("No differences")
else:
	print(result)
