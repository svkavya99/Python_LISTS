#TO REMOVE ALL THE OCCURANCES OF ELEMENTS IN LIST
list=[1,2,2,3,3,4,4,5,6]
print(list)
n=int(input("enter the element to e removed from list"))
i=0
length=len(list)
while(i<length):
    if(list[i]==n):
        list.remove(list[i])
        length=length-1
        continue
    i=i+1
print("list after removing elements:")
print(list)
