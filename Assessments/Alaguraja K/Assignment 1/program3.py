upper = int(input("Enter the upper value:"))
for number in range(2,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
