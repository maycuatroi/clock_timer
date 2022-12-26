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
    assert logger.log['my_function'] > 1