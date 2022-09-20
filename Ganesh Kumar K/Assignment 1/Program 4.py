n=int(input("Enter the number of terms : "))
t1=0
t2=1
if(n<=0):
    print("Invalid number of terms specified")
else:
    if n==1:
        print(t1)
    else:
        print(t1)
        print(t2)
        for i in range(n-2):
            c=t1+t2
            print(c)
            t1=t2
            t2=c
