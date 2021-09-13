import random
from datetime import datetime
import contextlib
import inspect
import io
l = []
def task2_decorator(decorator_argument):
    def wrapper_function(*args,**kwargs):
        global l
        wrapper_function.calls += 1
        start_time = datetime.now()
        with contextlib.redirect_stdout(io.StringIO()) as function_:
            output = decorator_argument(*args,**kwargs)
        end_time = datetime.now()
        s = function_.getvalue()

        execution_time = str(end_time-start_time).split(':')[-1]

        print(f'{decorator_argument.__name__} call {wrapper_function.calls} executes {execution_time} sec')
        print(f'NAME: \t{decorator_argument.__name__}')
        print(f'Type: \t{type(decorator_argument)}')
        print(f'Sign: \t{decorator_argument.__code__.co_varnames}')
        print(f'Args: \t{decorator_argument.__code__.co_argcount}')
        print(f'\t\tpositional {args}\n\t\tkey=worded {decorator_argument.__kwdefaults__}')
        print(f'Doc:  \t{decorator_argument.__doc__}')
        print(f'Source: \n{inspect.getsource(decorator_argument)}')

        print(f'Output: {output}')
        print(s)

    wrapper_function.calls = 0
    return wrapper_function
