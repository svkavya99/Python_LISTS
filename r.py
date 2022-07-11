my=[]
length=int(input("enter no.of elements"))
for i in range(0,length):
    my.append(int(input()))
print(my)
y=len(my)
for x in range(0,y):
    for n in range(x+1,y):
        if(my[x]==my[n]):
            my.remove(my[x])
            y=y-1
print(my)   



