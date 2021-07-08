"""
Church encoding of Boolean

Author: Minsoo Kim<km19809@users.noreply.github.com>
"""
from typing import Callable, Any
from inspect import signature


class Lambda():
    """
    Helper Class for debugging.\n
    Use function rather than this.
    """
    def __init__(self, function: Callable, name: str = "") -> None:
        """
        Initialize lambda.\n
        :params\n
        function lambda function for __call__ method.\n
        name debugging name of lambda.
        """
        self.__lambda = function
        self.__signature = signature(self.__lambda)
        self.__name = name if name else "".join((
            "λ", ".λ".join(self.__signature.parameters), "."))

    def __call__(self, *args: Any) -> Any:
        return self.__lambda(*args)

    def __str__(self) -> str:
        return f"{self.__name}{self.__signature}"

    def __repr__(self) -> str:
        return f"Lambda(f{self.__signature}, {self.__name})"

class Bool(Lambda):
    """
    Helper Class for debugging.\n
    Used for T(true) and F(false).
    """
    def __init__(self, function: Callable) -> None:
        """
        Initialize lambda.\n
        :params\n
        function lambda function for __call__ method.\n
        """
        super().__init__(function, "Bool")

    def __call__(self, *args: Any) -> Any:
        return super().__call__(*args)

    def __str__(self) -> str:
        return f"{self.eval()}"

    def __repr__(self) -> str:
        return f"Bool(f{self.__signature})"

    def eval(self)->bool:
        return self("T", "F")

T = Bool(lambda a, _: a)
F = Bool(lambda _, b: b)

def IF(condition:Bool, then:Callable, _else:Callable):
    """
    Church encoding of if-then-else
    """
    return condition(then, _else)

def AND(left:Bool, right:Bool)->Bool:
    """
    Church encoding of AND
    """
    return left(right, left)

def OR(left:Bool, right:Bool)->Bool:
    """
    Church encoding of OR
    """
    return left(left, right)

def NOT(_input:Bool)->Bool:
    """
    Church encoding of NOT
    """
    return Bool(lambda a, b: _input(b, a))

def XOR(left:Bool, right:Bool)->Bool:
    """
    Church encoding of XOR
    """
    return Bool(lambda a, b: left(right(b, a), right(a, b)))
