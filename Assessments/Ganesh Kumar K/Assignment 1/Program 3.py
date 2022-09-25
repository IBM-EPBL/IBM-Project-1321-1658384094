n=int(input("Enter the upper limit : "))
for i in range(1,n+1):
    fa=0
    for j in range(1,n+1):
        if i%j==0:
            fa+=1
    if fa==2:
        print(i)
