str1=str( input("Enter any string : ") )
evenindex=[]
oddindex=[]
"""
for i in range( 0,len(str1) ):
    if( i%2==0 ):
        evenindex.append(str1[i])
    else:
        oddindex.append(str1[i])
"""
# not working while( i in range(0,len(str1)) ):
i=0
while(i<len(str1)):
    if (i % 2 == 0):
        evenindex.append(str1[i])
    else:
        oddindex.append(str1[i])
    i+=1

print("All the even indexed elements : ",evenindex)
print("All the odd indexed elements : ",oddindex)
