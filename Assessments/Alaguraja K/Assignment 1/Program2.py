a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))

while(a < b + 1):
    if(a % 2 != 0):
        print(a)
    a+=1
