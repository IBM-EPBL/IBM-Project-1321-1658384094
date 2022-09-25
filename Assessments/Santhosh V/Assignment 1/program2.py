s = int(input("Enter the start number:"))
e = int(input("Enter the end number:"))
for n in range(s,e+1):
    if n % 2 != 0:
        print(n)
