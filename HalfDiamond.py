"""for i in range(0,4):
    for j in range(0,4):
        if(i==j):
            print("*",end=" ")
        elif(j>i):
            print(end=" ")
        else:
            print("*",end=" ")
    print()

for k in range(3,0,-1):
    for m in range(0,k):
            print("*",end=" ")
    print()
"""
"""
i,j= 0,0
while(i<4):
    while(j<4):
        if(i==j):
            print("*",end=" ")
        elif(i>j):
            print("*",end=" ")
        else:
            print(end=" ")
        j+=1
    print()
    j=0
    i+=1


k,l=3,0
while(k>0):
    while(l<k):
        print("*",end=" ")
        l+=1
    print()
    k-=1
    l=0
"""
def printPattern():
    i,j=0,0

    while( i<7 ):
        while( j<4 ):
            if( i==3 or j==0 ):
                print("*",end=" ")
            elif ( (i in [1,5])  and (j in [0,1]) ):
                print("*", end=" ")
            elif ((i in [2,4]) and (j in [0,1,2])):
                print("*", end=" ")
            else:
                print(" ", end=" ")
            j+=1
        print()
        j=0
        i+=1


i = True
while (i):
    str1 = str(input("Do you want to print pattern(y/n) : "))

    if (str1 in ['y', 'Y', "yes", "YES"]):
        printPattern()
    elif (str1 in ['n', 'N', "no", "NO"]):
        i = False
        print("Exiting code")
    else:
        print("Wrong input try again")

