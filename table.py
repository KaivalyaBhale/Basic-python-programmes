table=[]
stable=[]

for i in range(1,11):
    for j in range(1,11):
            stable.append( i*j )
    table.insert(i,stable)
    stable=[]

"""
single line format
print(table)

#horizontal format
for i in range(0,10):
    print(table[i])

"""
#row and coloum format
for k in range(0,10):
    for l in range(0,10):
        print( table[k][l],end="\t" )
    print()
