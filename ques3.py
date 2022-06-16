#program to write the shorter route using conditional statements and logical operators.
a=10
b=15
shorter_route=0
if a<b:
    shorter_route=10
    print("Hey this is the shorter route to go to the college")
else:
    shorter_route=15
    print("Hey it covers longer distance")
print(f"This route will take to your college within short distance of {shorter_route} Km.")

a=10
b=15
if a==b:
    print(" Both Distances are same ")
elif a>b and b<=a:
    print("Both distances arent same.")
elif a!=b:
    print("Both distances are not same.")
else:
    print("none")