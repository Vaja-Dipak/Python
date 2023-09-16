'''
- Syntax


if condition:
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement
'''

s1=int(input("Enter marks of Subject 1 : "))
s2=int(input("Enter marks of Subject 2 : "))
s3=int(input("Enter marks of Subject 3 : "))
s4=int(input("Enter marks of Subject 4 : "))

total=s1+s2+s3+s4
per=total/4

print("Total = ",total)
print("Percentage = ",per)

if per>=90:
    print("Distinction")
elif per>=75:
    print("First Class")
elif per>=55:
    print("Second Class")
elif per>=40:
    print("Therd Class")
elif per>=27:
    print("Pass Class")
else:
    print("Fail")