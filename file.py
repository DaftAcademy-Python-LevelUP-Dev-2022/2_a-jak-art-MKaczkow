# TASK 1
def greeter(func):
    def wrapper_function(*args, **kwargs):
        result = func(*args, **kwargs)
        result = 'Aloha ' + result.title()
        return result
    return wrapper_function


# TASK 2
def sums_of_str_elements_are_equal(func):
    def wrapper_function(*args, **kwargs):
        first_num, second_num = func(*args, **kwargs).split()
        first_negative, second_negative = False, False

        if first_num[0] == '-':
            first_num = first_num[1:]
            first_negative = True
        if second_num[0] == '-':
            second_num = second_num[1:]
            second_negative = True
            
        first_sum = sum(int(digit) for digit in first_num)
        second_sum = sum(int(digit) for digit in second_num)

        if first_negative:
            first_sum *= -1
        if second_negative:
            second_sum *= -1 
            
        if first_sum == second_sum:
            result = f'{first_sum} == {second_sum}'
        else:
            result = f'{first_sum} != {second_sum}'
        
        return result 
    return wrapper_function


# TASK 3
def format_output(*required_keys):
    def true_decorator(func):
        def wrapper_function(*args, **kwargs):
            required_keys_list = list(required_keys)
            func_output = func(*args, **kwargs)
            result = dict.fromkeys(required_keys_list, "")

            for key in result:
                if '__' in key:
                    keys_list = key.split(sep='__')
                    if not all(item in func_output for item in keys_list):
                        raise ValueError
                    concat_value = ""
                    for sub_key in keys_list:
                        concat_value += f'{func_output[sub_key]} '
                    result.update({key: concat_value.strip()})
                elif key not in func_output:
                    raise ValueError
                else:
                    result.update({key: func_output[key]})
            
            for key, value in result.items():
                if value == '':
                    result.update({key: "Empty value"})

            return result
        return wrapper_function
    return true_decorator


# TASK 4
from functools import wraps


def add_method_to_instance(klass):
    def true_decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            return func()
        
        setattr(klass, func.__name__, wrapper_function)

        return func 
    return true_decorator
