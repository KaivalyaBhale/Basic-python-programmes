def printPattern():
    for i in range(0,7):
        for j in range(0,7):

            if( i==3 or j==3 ):
                print("*",end=" ")
            elif( (i in [1,5]) and ( j in [2,3,4]) ):
                print("*",end=" ")
            elif( (i in [2,4]) and ( j in [1,2,3,4,5])):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

i=True
while(i):
    str1=str( input("Do you want to print pattern(y/n) : ") )

    if(str1 in ['y','Y',"yes","YES"]):
        printPattern()
    elif(str1 in ['n','N',"no","NO"]):
        i=False
        print("Exiting code")
    else:
        print("Wrong input try again")

