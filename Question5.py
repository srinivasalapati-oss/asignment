#python program to sum the elements of list  
list=[]
a=5
i=1
while i<=a:
    n=int(input("Enter the values"))
    list.append(n)
    i=i+1
print(list)
i=0
while i<len(list):
    print("Elements are",i+1,list[i])
    i=i+1
i=0
n=0
while(n<len(list)):
    i=i+list[n]
    n=n+1
print("sum of all elements in list:",i)