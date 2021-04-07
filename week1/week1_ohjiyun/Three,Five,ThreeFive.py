n = int(input('Enter the number : '))

if (n%3==0 and n%5==0):
    print("ThreeFive")
elif (n%3==0):
    print("Three")
elif (n%5==0):
    print("Five")
else:
    print(n)
