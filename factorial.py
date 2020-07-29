import sys
import time
sys.setrecursionlimit(3507)
num=int(sys.argv[1])
def factorial(num):
    total = 1
    if num == 1:
        return total
    else:
        total = factorial(num-1)
        total *= num
        return total

starts = time.time()
print(factorial(num))
ends = time.time() - starts
print(ends)