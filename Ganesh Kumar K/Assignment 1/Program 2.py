a,b=map(int,input("Enter the interval : ").split())
i=a
while(i>=a and i<=b):
    if i%2!=0:
        print(i)
    i+=1
