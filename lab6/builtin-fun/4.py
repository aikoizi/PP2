import time
import math

def square(num,millisec):
    x = math.sqrt(num)
    time.sleep(millisec/1000)
    print(f'Square root of {num} after {millisec} miliseconds is {x}')

square(25100, 2123)
