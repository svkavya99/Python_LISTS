list=[]
n=int(input("enter no.of elements in list"))
for i in range(n):
    my=int(input("enter the elements in list"))
    list.append(my)
listodd=[]
listeven=[]
for n in list:
    if n%2==0:
        listeven.append(n)
    else:
        listodd.append(n)
print("given list",list)
print("even elements in list",listeven)
print("odd elements in list",listodd)
