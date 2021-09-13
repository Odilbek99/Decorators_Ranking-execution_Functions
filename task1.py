import random
from datetime import datetime
import contextlib
import io
l = []
def task1_decorator(decorator_argument):
    def wrapper_function(*args,**kwargs):
        global l
        wrapper_function.calls += 1
        start_time = datetime.now()
        with contextlib.redirect_stdout(io.StringIO()) as function_:
            decorator_argument(*args,**kwargs)
        end_time = datetime.now()
        execution_time = str(end_time-start_time).split(':')[-1]
        return f'{decorator_argument.__name__} call {wrapper_function.calls} executes {execution_time} sec'

    wrapper_function.calls = 0
    return wrapper_function