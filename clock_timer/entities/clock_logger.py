import time


class ClockLogger:
    def __init__(self, logger_function=None, log_callback=None):
        self.log = {}
        if logger_function is not None:
            self.logger_function = logger_function
        else:
            self.logger_function = print
        self.log_callback = log_callback
        self.start = None
        self.end = None
        self.total_elapsed = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            self.total_elapsed += elapsed
            function_name = func.__name__
            args = [str(arg) for arg in args]
            kwargs = [f"{key}={value}" for key, value in kwargs.items()]
            args = ", ".join(args)
            kwargs = ", ".join(kwargs)

            if function_name not in self.log:
                self.log[function_name] = []
            self.log[function_name].append((args, kwargs, elapsed))
            call_count = len(self.log[function_name])
            self.logger_function(
                f"{function_name} was called {call_count} times, "
                f"total time elapsed: {elapsed:.3f}s"
            )
            if self.log_callback:
                self.log_callback(
                    function_name=function_name,
                    call_count=call_count,
                    elapsed_time=elapsed,
                    total_elapsed_time=self.total_elapsed,
                    function_args=args,
                    function_kwargs=kwargs,
                )

            return result

        return wrapper

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.total_elapsed = self.end - self.start
        self.logger_function(f"Total time elapsed: {self.total_elapsed:.6f}s")

    def __str__(self):
        if self.log:
            for key, value in self.log.items():
                self.logger_function(
                    f"{key} was called {value[0]} times, total time elapsed: {value[1]:.6f}s"
                )
        else:
            self.logger_function(f"Total time elapsed: {self.total_elapsed:.6f}s")
