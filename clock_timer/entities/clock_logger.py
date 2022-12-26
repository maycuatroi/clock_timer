import time


class ClockLogger:
    def __init__(self, logger_function=None):
        self.log = {}
        if logger_function is not None:
            self.logger_function = logger_function
        else:
            self.logger_function = print
        self.start = None
        self.end = None
        self.elapsed = None

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            if func.__name__ not in self.log:
                self.log[func.__name__] = [0, 0]
            self.log[func.__name__][0] += 1
            self.log[func.__name__][1] += elapsed
            self.logger_function(
                f"{func.__name__} was called {self.log[func.__name__][0]} times, total time elapsed: {self.log[func.__name__][1]:.6f}s"
            )
            return result

        return wrapper

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        self.logger_function(f"Total time elapsed: {self.elapsed:.6f}s")
