list=[]
n=int(input("enter the no.of elements in list"))
for i in range(n):
    item=int(input("enter the elements"))
    list.append(item)
    print(list)
k=int(input("enter the element index to be find"))
print(list.index(k))


