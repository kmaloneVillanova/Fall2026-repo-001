print("hello world!")

# this is a comment

'''
this is one line
this is the second line
this is a function
'''

# this is a lines
# this is another line

x = 100
print(x)

x = 105
x=5.5
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
z=x/y
z=int(z)
print(z)

result=x//y
print(result)

min_value=min(10,2)
print(min_value)
raised=pow(4,2)
print(raised)
raised=4**2

if x<0:
    print("x is less than 0")
    print("second line of code")

if x<0 and y<0:
    print("both less than 0")

if x<0 or y<0:
    print("at least one less than 0")

if x<0:
    print("less than 0")
elif x>0:
    print("greater than 0")
else:
    print(0)

counter=0
while counter < 10:
    print(counter)
    counter += 1

for i in range(1,5):
    print(i)

lst=[1,2,3,4,5]
for i in range(5):
    print(i,lst[i])

for i in range(len(lst)):
    print(i, lst[i])

for i in range(len(lst)-1,-1,-1):
    print(i, lst[i])

for i,val in enumerate(lst):
    print(i, val)

for value in lst:
    print(value)

def hello(name="Bob"):
    print("hello", name)
hello("Alice")

full_name="Kathleen Marie Malone"
first_name=full_name[:8]
last_name=full_name[16:]
middle_name=full_name[9:14]

