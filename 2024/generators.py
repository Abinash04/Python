def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator in a for loop
for i in countdown(5):
    print(i, end=' ')  # Output: 5 4 3 2 1
