name = "college"
age = 24 
isWalking = True
height = 5.6
print(name, "belongs to", type(name))
print(age, "belongs to",type(age))
print(isWalking, "belongs to",type(isWalking))
print(height, "belongs to",type(height))

for i in range(10,0, -1):
    print(i)

i =0
while i < 3:
    print("Hello World!")
    i+=1


friends = ['f1', 'f2', 'f3', 'f4', 'f5']
friends.pop()
del friends[1]
print(friends)


marks = (39,84,81,69,50)
print(type(marks))
marks = list(marks)
print(type(marks))

def add(a:int, b:int):
    return a+b

print(add(4,5))

for i in range(0,51,2):
    print(i,end=' ')