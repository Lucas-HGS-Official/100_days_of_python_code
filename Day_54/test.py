import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    start_time = time.time()
    function()
    end_time = time.time()

    print(end_time - start_time)


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
