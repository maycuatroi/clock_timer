# Clock Timmer

[![CI](https://github.com/maycuatroi/clock_timer/actions/workflows/main.yml/badge.svg)](https://github.com/maycuatroi/clock_timer/actions/workflows/main.yml)

Clock Timmer is a Python library that provides a tool for logging the time and number of calls of a function in Python. It can be used as a decorator or context manager, allowing you to log the time and number of calls of a function or block of code without modifying any lines of code within the function or block.

Installation
To install Clock Timmer, use the following command:
```commandline
pip install python-clock-timer
```
# Usage
## As a decorator
To use Clock Timmer as a decorator, you can use it like this:

```python
from clock_timer import ClockLogger

logger = ClockLogger()

@logger
def my_function():
    # code of the function
```
After using the decorator, you can access the time and number of calls logs of the function by accessing the log attribute of the Clock Timmer object. For example, to get the number of calls and total time elapsed of the my_function, you can do the following:

```python
print(logger.log['my_function'])
```
## As a context manager
To use Clock Timmer as a context manager, you can use it like this:

```python
from clock_timer import ClockLogger

with ClockLogger() as logger:
# code of the block

print(logger.total_elapsed)
```
After using the context manager, you can access the total time elapsed by accessing the elapsed attribute of the Clock Timmer object.

# Example
Here is an example of using Clock Timmer as a decorator and a context manager:

```python
from clock_timer import ClockLogger
import time

# Using Clock Timmer as a decorator
logger = ClockLogger()

@logger
def my_function():
    time.sleep(1)

my_function()
my_function()

print(logger.log['my_function'])
```
the output
```
my_function was called 1 times, total time elapsed: 1.005031s
my_function was called 2 times, total time elapsed: 2.005123s
[2, 2.0051226250000003]
```

## Using Clock Timmer as a context manager

```python
import time

from clock_timer import ClockLogger

with ClockLogger() as logger:
    time.sleep(1)

print(logger.total_elapsed)
```
The output of this example will be:

```
Total time elapsed: 1.003622s
1.003622042
```
# Contributing
We welcome contributions to Clock Timmer. If you have any ideas for improvements or want to report a bug, please open an issue or submit a pull request.

# License
Clock Timmer is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
