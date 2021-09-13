import cmath


from task1 import task1_decorator
from task2 import task2_decorator
from task3 import task3_decorator
from task4 import task4_decorator

# FUNCTION 1
# Pascals triange
def f1(n:int) -> None:
            '''This function prints Pascal's triangle'''
            r1, r2 = [1], [1, 1]
            degree = 1
            while degree <= n:
                print(r1)
                r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:])] + [1]
                degree += 1



# FUNCTION 2
# Quadratic equation
def f2(a,b,c):
    '''This function prints result of quadratic
        equation(x1,x2). It takes three arguments
        (a,b,c). To variables x and x2 assigned the
        formula of quadratic equation.'''
    print(f'{a}x**2 + {b}x + {c}')
    delta = (b*b)-(4*a*c)
    x = (-b+(cmath.sqrt(delta)))/2*a
    x2 = (-b-(cmath.sqrt(delta)))/2*a
    return f'x1={x}\n\tx2={x2}'
    
# FUNCTION 3
# Sum of arbitrary arguments
f3 = lambda *args: sum(args)
f3.__name__ = 'f3'
f3.__doc__ = '''This function takes arbitrary number of 
        parameters and prints sum of these arguments'''
# FUNCTION 4
# Prime numbers
f4 = lambda d, f, g : d + f + g
f4.__name__ = 'f4'
f4.__doc__ = '''This function same as previous function. 
            But in this function we can assign only three numbers as argument of function. 
            The function prints the sum of these three arguments'''




if __name__ == '__main__':
    print('---------------------------------------------------------TASK 1---------------------------------------------------------')
    task1_f1 = task1_decorator(f1)
    task1_f2 = task1_decorator(f2)
    task1_f3 = task1_decorator(f3)
    task1_f4 = task1_decorator(f4)


    for i in range(1,5):
        print('TASK 1 TEST', i)
        print(task1_f1(15))
        print(task1_f2(1,4,10))
        print(task1_f3(44,56,7))
        print(task1_f4(25,45,32))

    print('---------------------------------------------------------TASK 2---------------------------------------------------------')
    task2_f1 = task2_decorator(f1)
    task2_f2 = task2_decorator(f2)
    task2_f3 = task2_decorator(f3)
    task2_f4 = task2_decorator(f4)


    for i in range(1, 5):
        print('TASK 2 TEST', i)
        print(task2_f1(15))
        print(task2_f2(1, 4, 10))
        print(task2_f3(44, 56, 7))
        print(task2_f4(100,200,44))



    print('---------------------------------------------------------TASK 3---------------------------------------------------------')
    task3_f1 = task3_decorator(f1)
    task3_f2 = task3_decorator(f2)
    task3_f3 = task3_decorator(f3)
    task3_f4 = task3_decorator(f4)

    task3_f1(15)
    task3_f2(1, 4, 10)
    task3_f3(44, 56, 7)
    task3_f4(100,200,44)
    print('TESTING FOR CLASS AND FUNCTION DECORATORS')
    task3_decorator.table(task3_decorator)

    print('---------------------------------------------------------TASK 4---------------------------------------------------------')
    task4_f1 = task4_decorator(f1)
    task4_f2 = task4_decorator(f2)
    task4_f3 = task4_decorator(f3)
    task4_f4 = task4_decorator(f4)

    print("NORMAL TESTNG")
    task4_f1(15)
    task4_f2(1, 4, 10)
    task4_f3(44, 56, 7)
    task4_f4(100, 200, 44)
    task4_decorator.table(task4_decorator)

    task4_f1()
    task4_f2(1, 4)
    task4_f3('a')
    task4_f4(200, 44)
    print('TESTING FOR CLASS AND FUNCTION DECORATORS')
    print('TASK 4 TESTING WITH ERRORS')

    print("All errors are dumped to task4_errors.txt file")


