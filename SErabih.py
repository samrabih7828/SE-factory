# Let's do some basic math
x = 5
y = 10

# Adding two numbers
sum = x + y
print("The sum of", x, "and", y, "is:", sum)


# new code 
z=10 
q=5
print(z%q)


condition = "nizar" 
condition2 = "nizar"
if condition == condition2:
    print("hi")


condition3 = True
condition4 = False 
if condition3 or condition4:
    print("hello")


Raining= True
Sunny= False 
if Raining and Sunny:
    print("happy")


# let's write a program that reads 3 inputs then sort them in ascending order a <= b <=c:
# Suppose a=5, b=3, c=7
a=7
b=7
c=5
# using only <,>
# a= int(input ("please insert a number"))
# b= int(input ("please insert b number"))
# c= int(input ("please insert c number"))
if a>b:
    a,b = b,a
if a > c:
    c,a = a,c
if b>c:
    b,c = c,b
print (a,b,c)


grade=54
if (grade> 95):
    print ("A+")
elif(grade> 90):
    print ("A")
else: print("failed")


x=0
sum=0
while (x<4):
    x=x+1
sum=sum + x
print(x,sum)

# x=0 true x=1
# x=1 true x=2
# x=2 true x=3
# x=3 true x=4



x=5
sum=0
while (x>0):
    x=x-1
sum=sum - x
print(x,sum)
