import random
from datetime import datetime
from contextlib import redirect_stdout
import contextlib
import inspect
import io


class task3_decorator:

    d = {}
    def __init__(self, decorator_argument):
        self.calls = 0
        self.decorator_argument = decorator_argument


    def __call__(self,*args):
        self.args = locals()
        self.calls += 1

        with open('output_programs_task3.txt', 'a') as file:
            with redirect_stdout(file) as f:  # puts functions outputs into text.txt file
                with redirect_stdout(io.StringIO()) as s:
                    start_time = datetime.now()
                    output = self.decorator_argument(*args)
                    end_time = datetime.now()
                get_value = s.getvalue()
                execution_time = str(end_time - start_time).split(':')[-1]

                print(f'{self.decorator_argument.__name__} call {self.calls} executes {execution_time} sec')
                print(f'Name: \t{self.decorator_argument.__name__}')
                print(f'Type: \t{type(self.decorator_argument)}')
                print(f'Sign: \t{self.decorator_argument.__code__.co_varnames}')
                print(f'Args: \t{self.decorator_argument.__code__.co_argcount}')
                print(f'\t\tpositional {args}\n\t\tkey=worded {self.decorator_argument.__kwdefaults__}')
                print(f'Doc:  \t{self.decorator_argument.__doc__}')
                print(f'Source: \n{inspect.getsource(self.decorator_argument)}')

                print(f'Output: {output}')
                print(s)
                task3_decorator.d[(self.decorator_argument.__name__, id(self.decorator_argument))] = execution_time

    def table(self):
        all_functions = dict(sorted(task3_decorator.d.items(), key=lambda item: item[1]))
        print('PROGRAM | RANK | TIME ELAPSED')
        count = 1
        for i in all_functions:
            print(i[0], '\t', count, '\t', float(all_functions[i]) * 1000, 'seconds')
            count += 1
