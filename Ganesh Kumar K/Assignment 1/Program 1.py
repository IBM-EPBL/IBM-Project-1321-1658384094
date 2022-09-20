n=int(input("Enter the number : "))
fa=0
for i in range(1,n+1):
    if(n%i==0):
        fa=fa+1
    
if(fa==2):
    print("{} is a Prime Number".format(n))
else:
    print("{} is a not a Prime Number".format(n))
