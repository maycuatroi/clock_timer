from clock_timer import ClockLogger
import time

# Using Clock Logger as a decorator
logger = ClockLogger()

@logger
def my_function():
    time.sleep(1)

my_function()
my_function()

print(logger.log['my_function'])