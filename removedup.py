list1=[]
list2=[]
n=int(input("enter no.of elements"))
for i in range(n):
    mylist=int(input("enter the elements in list"))
    list1.append(mylist)
for n in list1:
    if n not in list2:
        list2.append(n)
print(list2)        
