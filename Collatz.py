def Collatz(Num):
    if Num==1:
        return
    if Num % 2 == 1:
        newNum=int(Num*3+1)
    else:
        newNum=int(Num/2)
    print(newNum)
    Collatz(newNum)
#------------------------------------
Num = input("Enter your value: ")
try:
    val = int(Num)
    if val < 0 :
        print("Error: Please enter a positive Integer")
        exit(1)
except ValueError:
    print("Error: Please enter a Positive integer")
    exit(1)

Collatz(int(Num))
