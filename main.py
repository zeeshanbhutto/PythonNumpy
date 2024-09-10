#hy so today i am here again to learn about pandas and numpy
name=input("what is your name:- ")
print("hello "+name.upper())

first=input("enter you first numbr: ")
second=input("enter your second numbr: ")
sum=int(first) + int(second)
print("Addition of two numbrs",sum)
#okk now we are going to build a simple calculator
number1=int(input("enter your first numb: "))
number2=int(input("enter your second numb: "))
operator=input("enter your operator(+,-,*,/): ")

if operator=="+":
    print(number1 + number2)
elif operator=="-":
    print(number1 - number2)
elif operator=="*":
    print(number1 * number2)
elif operator=="/":
    print(number1 / number2)
else:
    print("enter a valid numbr")
#okk great now we are going to see loops in python
print("")
i=1
while i<=5:
    print(i)
    i=i+1
a=1
for a in range(10):
    print(a * "*")
    a=a+1
students=["zeeshan","saba","sana","hussnain","zulqurnain","Areeba"]
for students in students:
    if students=="hussnain":
     continue;
    print(students)
#now we are going t0 revice the functions topic in python
from math import sqrt
print(sqrt(5))
#okk we will contine it again and today any hoe start pandas! detailed