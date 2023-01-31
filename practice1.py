mylist = ['apple', 'oranges', 'melon']
print(mylist[2])

mypackinglist = [['book', 'pen'], ['cup', 'spoon']]
print(mypackinglist)

for x in mylist:
    print(x)
    if x=='oranges':
        break
for x in 'leila':
    print(x)

for x in mylist:
    if x=='oranges':
        continue
    print(x)

for x in range(10,20,2):
    print(x)
a=3
b=4
while  b>a:
    print('b is greater than a')
    break

def Greeting(name):
    print('Hello ' + name)
Greeting('Leila')

def myfunction(food):
    for x in food:
        print(x)

fruits=['mango','apple','melon']
myfunction(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Greeting(self):
        print('Hello , Iam ' + self.name)


P1 = Person('Leila',21)
P1.Greeting()
n=4
#for i in range(n):
    #for j in range(i+1):
        #print(1, end='')
    #print()
s=3
n=4
for i in range(n):
    s=s+"1"
print(s)








