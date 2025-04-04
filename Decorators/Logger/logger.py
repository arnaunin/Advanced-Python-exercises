import time

def logger(func):
    def wrapper():
        start_time = time.time()
        print(f"Invoking the function '{func.__name__}'...")

        try:
            result = func()
        except Exception as e:
            print(f"An error has occurred in the function '{func.__name__}': {e}")
            raise

        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time} seconds to run.")

        return result
    return wrapper

@logger
# Main function, calculates some numbers of fibonacci series
def fibonacci():
    fib_series = [0,1]
    for i in range(2,20):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

print(f"Function results: {fibonacci()}")