#python program to define five variables
print("Hello this is python module,welcome to the world of python")
print("Hey programmer lets swap the variables")
a=input("Enter a value")
b=input("Enter b value")
c=input("Enter c value")
d=input("Enter d value")
e=input("Enter e value")
print("The value of a is {}",format(a))
print("The value of b is {}",format(b))
print("The value of c is {}",format(c))
print("The value of d is {}",format(d))
print("The value of e is {}",format(e))
temp_var=a
a=b
b=c
c=d
d=e
e=temp_var
print("The value of a after swapping is {}".format(a))
print("The value of b after swapping is {}".format(b))
print("The value of c after swapping is {}".format(c))
print("The value of d after swapping is {}".format(d))
print("The value of e after swapping is {}".format(e))



            #or
print("Hello welcome to the world of python")
a=5
b=10.5
c=11
d=13
e=14
a,b=b,a
b,c=c,b
c,d=d,c
d,e=e,d
print(a)
print(b)
print(c)
print(d)
print(e)