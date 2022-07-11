# READ N ELEMENTS FROM USER FOR LIST AND PRINT THE LIST 
list=[]
n=int(input("enter the no.of elements"))
#list=int(input("enter the elements of list"))
for i in range(0,n):
    k=int(input("enter the elements of list"))
    list.append(k)
for i in range(0,n):
    print(list[i])
