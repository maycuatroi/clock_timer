import time

from clock_timer import ClockLogger

with ClockLogger() as logger:
    time.sleep(1)

print(logger.elapsed)
