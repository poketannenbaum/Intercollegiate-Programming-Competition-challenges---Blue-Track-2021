originalnumber = input("Enter a positive number: ")
middlemannumber = originalnumber
while (True):
    gladcomponents = list(middlemannumber)
    gladcomponents = [int(num) for num in gladcomponents]
    
    placeholdernumber = 0  
    
    for number in gladcomponents:
        number = number * number
        placeholdernumber += number
    
    if originalnumber == placeholdernumber:
        print("Not a Glad Number")
        break
    elif placeholdernumber == 1:
        print("Glad Number")
        break
    else:
        middlemannumber = str(placeholdernumber)  