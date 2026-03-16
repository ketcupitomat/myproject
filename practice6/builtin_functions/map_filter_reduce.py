from functools import reduce

nums = [1, 2, 3, 4, 5, 6]


squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)


evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)


total = reduce(lambda x, y: x + y, nums)
print("Sum:", total)