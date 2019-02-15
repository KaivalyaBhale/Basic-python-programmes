"""
for i in range(1,9):
    for j in range(1,8):
        if( i==1 or i==8 or j==4 ):
            print("*",end=" ")
        elif( i==2 and ( j in [2,3,4,5,6] ) ):
            print("*",end=" ")
        elif (i==3 and (j in [3, 4, 5,])):
            print("*", end=" ")
        elif (i==6 and (j in [3, 4, 5,])):
            print("*", end=" ")
        elif (i == 7 and (j in [2, 3, 4, 5, 6])):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()
"""
def printPattern():
    i=j=0
    while(i<8):
        while(j<7):
            if( (i in [0,7] )or j==3 ):
                print("*",end=" ")
            elif( ( i in [1,6]) and ( j in [1,2,3,4,5,] ) ):
                print("*",end=" ")
            elif( (i in [2,5]) and (j in [2,3, 4])):
                print("*", end=" ")
            else:
                print(" ",end=" ")

            j+=1
        print()
        i+=1
        j=0


i = True
while (i):
    print()
    str1 = str(input("Do you want to print pattern(y/n) : "))

    if (str1 in ['y', 'Y', "yes", "YES"]):
        print();        printPattern()
    elif (str1 in ['n', 'N', "no", "NO"]):
        i = False
        print("Exiting code")
    else:
        print("Wrong input try again")


