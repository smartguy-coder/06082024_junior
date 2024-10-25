

def wrap_result_decorator(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        modified_result = {'result': result}
        return modified_result

    return wrapper


@wrap_result_decorator
def determines_the_path_traveled(time_in_action: float, speed: float) -> float:
    total_distance = time_in_action * speed
    return float(total_distance)


@wrap_result_decorator
def calculate_rectangle_square(width: float, hight: float) -> float:
    square = width * hight
    return float(square)


@wrap_result_decorator
def return_empty_list() -> list:
    return []


print(determines_the_path_traveled(10, 100))
print(return_empty_list())