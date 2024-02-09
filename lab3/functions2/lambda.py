#Example1
x = lambda a : a + 10
print(x(5))

#Example2
x = lambda a, b : a * b
print(x(5, 6))

#Example3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Example4
def myfunc(n):
  return lambda a : a * n

#Example5
def myfunc(n):
  return lambda a : a * n

#Example6
mydoubler = myfunc(2)

print(mydoubler(11))

#Example7
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#Example8
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Exercise1
x = lambda a : a