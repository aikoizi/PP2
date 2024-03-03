from functools import reduce

list = [6, 4, 7, 11, 5]
def multiply(x, y):
    return x * y

result = reduce(multiply, list)


print("Result:", result)
