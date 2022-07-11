num=[]
sq=[]
cub=[]
start=int(input("enter start value"))
end=int(input("enter end value"))
for i in range(start,end+1):
    num.append(i)
    sq.append(i**2)
    cub.append(i**3)
print("numbers in list",num)
print("squares",sq)
print("cub",cub)
