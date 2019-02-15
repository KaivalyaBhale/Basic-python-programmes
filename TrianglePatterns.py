
def lowerTriangle(n):
    for i in range(1,n+1):
        for j in range(0,i):
                print("*",end=" ")
        print(" ")

def upperTriangle(n):
    for i in range(n,0,-1):
        for j in range(0,i) :
            print("*",end=" ")
        print()

i = True
while (i):
    print()
    str1 = str(input("Do you want to print pattern(Upper/lower/both/no) : "))
    ino = int(input("Enter any number :"))
    if (str1 in ['upper',"Upper",'UPPER','u',"U"]):
        upperTriangle(ino)
    elif (str1 in ['lower', 'LOWER', "Lower", "l","L"]):
        lowerTriangle(ino)
    elif(str1 in ["both","b","B"]):
        lowerTriangle(ino)
        upperTriangle(ino)
    elif (str1 in ['n', 'N', "no", "NO"]):
        i = False
        print("Exiting code")
    else:
        print("Wrong input try again")
