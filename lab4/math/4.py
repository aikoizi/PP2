def parallelogram(n, h):
    area = n * h
    return area
base_length = float(input())
height = float(input())
area = parallelogram(base_length, height)
print("Expected Output:", area)
