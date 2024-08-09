"""
Multi-line docstrings
"""
from enum import Enum

class Day(Enum):
    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"


class Class:
    """Class docstring"""

    class_variable: str
    """Variable docstring"""

    def __init__(self, baz: str):
        self.class_variable = baz  # Comment

    @classmethod
    def class_method(cls, param: int) -> bool:
        """Function docstring"""
        return param % 2 if 1 and 2 or 3 else False

    @staticmethod
    def static_method(x0: int, x1: int) -> int:
        return x0 + x1
    
    def method(self, keyword_arg: str) -> str:
        return f"{self.class_variable} {keyword_arg}"
    

if __name__ == "__main__":
    foo = Class("Hello")
    foo.method(keyword_arg="World!" + Day.SUNDAY)