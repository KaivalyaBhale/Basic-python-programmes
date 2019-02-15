"""
for i in range(1,8):
    for j in range(1,9):

        if(j==1 or j==8 or i==4):                                   j in [1,8]
            print("*",end=" ")
        elif(i==2 and (j==2 or j==7)):                              (i==2 and (j in [2,7]))
            print("*",end=" ")
        elif (i == 3 and (j == 2 or j == 7 or j==3 or j==6)):       (i==3 and (j in [2,3,6,7]))
            print("*", end=" ")
        elif (i == 5 and (j == 2 or j == 7 or j==3 or j==6 )):      (i==5 and (j in [2,3,6,7]))
            print("*", end=" ")
        elif (i == 6 and (j == 2 or j == 7)):                       (i==6 and (j in [2,7]))
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
"""
def printPattern():
    i,j=0,0
    while(i<7):
        while(j<8):
            if((j in [0,7]) or i==3):
                print("*",end=" ")
            elif( (i in [1,5]) and (j in [1,6])):
                print("*",end=" ")
            elif ( (i in [2,4]) and (j in [1,2,5,6])):
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
