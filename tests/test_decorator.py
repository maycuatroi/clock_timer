import time

from clock_timer import ClockLogger


def test_decorator():
    """Test decorator"""
    logger = ClockLogger()

    @logger
    def my_function():
        time.sleep(1)

    my_function()
    my_function()
    my_function_logs = logger.log["my_function"]
    time_called = my_function_logs[0]
    time_elapsed = my_function_logs[1]
    assert time_called == 2
    assert time_elapsed > 1
