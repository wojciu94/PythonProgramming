from typing import Callable, Union


def dummy_operation(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a, b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def calculate(operation: Callable[[Union[int, float], Union[int, float]], Union[int, float]],
              a: Union[int, float], b: Union[int, float]) -> Union[int, float]:

    """
    def operation(a: Union [int, float], b: Union [int, float]) -> Union [int, float]:     a,b może być albo intem albo floatem
        pass
    def operation(a: Any, b:Any) -> Any:
        pass
    """

    return operation(a, b)


# print(calculate(dummy_operation, 1, 2))
# print(calculate(multiply, 1.0, 2.0))