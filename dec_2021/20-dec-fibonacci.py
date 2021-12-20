from timeit import default_timer as timer

## Missing number (warm-up)

#  array of unsorted nums constrained by index [1, 4, 5, 8, 7, 2, 3] len == 8
# 1 < x < n + 1   => n == len(arr)
# Q: find missing number

# Optimal Time: O(n)
# def findMissingNumber(arr):
#     count = 1
#     total = 0

#     for j in range(len(arr)):
#         total += count
#         total -= arr[j]
        
#         count += 1
#     total += count

#     return total


# example_arr = [1, 4, 5, 8, 7, 2, 3]  # ans: 6
# print(findMissingNumber(example_arr))


# Recursion - Fibonacci
# Given n => nth number of fib sequence
def fib1(n):
    fiblist = [0, 1]  # Storage O(n) heap memory

    while len(fiblist) <= n:
        next_fib = fiblist[-1] + fiblist[-2]
        fiblist.append(next_fib)

    return fiblist[-1]    

# dyanmic programming
table = {
    0: 0,
    1: 1,
}

def fib(n):
    if n <= 1:
        return n
    if n - 1 not in table:
        table[n - 1] = fib(n - 1)
    if n - 2 not in table:
        table[n - 2] = fib(n - 2)
    return table[n-1] + table[n-2]


def fib2(n):
    if n <= 1:
        return n
    return fib2(n-1) + fib2(n-2)


# 0 1 1 2 3 5 8 13 21 ...

start = timer()
fib2(30)
end1 = timer()
fib(30)
end2 = timer()
fib1(30)
end3 = timer()
print(f'fib recursive takes: {end1 - start}, fib dynamic takes: {end2 - end1}, fib iterative takes: {end3 - end2}')
