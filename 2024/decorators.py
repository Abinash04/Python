def count_calls(func):
    """Decorator to count the number of times a function is called."""
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"inside:{wrapper.calls}")

        print(f"Function '{func.__name__}' has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    print(f"outside:{wrapper.calls}")
    return wrapper

# Example usage:
@count_calls
def my_function():
    print("Inside my_function")

my_function()
my_function()
my_function()
