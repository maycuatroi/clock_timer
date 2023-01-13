import time

from clock_timer import ClockLogger


def test_context_action():
    """Test Context Action"""
    with ClockLogger() as logger:
        time.sleep(1)
    assert logger.total_elapsed > 0
