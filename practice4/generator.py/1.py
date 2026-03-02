def square_generator(N):
    for i in range(N + 1):
        yield i * i

# Example usage
for value in square_generator(5):
    print(value)