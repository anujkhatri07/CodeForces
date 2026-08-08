n=int(input())
i=0
count=0
 
for i in range(n):
    word=str(input())
    if word=='Tetrahedron':
        count+=4
    elif word=='Cube':
        count+=6
    elif word=='Octahedron':
        count+=8
    elif word=='Dodecahedron':
        count+=12
    elif word=='Icosahedron':
        count+=20
 
 
print(count)