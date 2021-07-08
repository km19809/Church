"""
Church encoding of numeral 

Author: Minsoo Kim<km19809@users.noreply.github.com>
"""
from typing import Callable
from .boolean import *

class Increment():
    """
    Functions that add an int to its input.\n
    Used for decode numeral church encoding.
    """
    def __init__(self, value:int=1) -> None:
        self.__value=value
    def __call__(self, function) -> Any:
        if function is None:
            return self
        elif isinstance(function, Increment):
            return Increment(self.__value+function.__value)
        else:
            return function+self.__value
    def __str__(self) -> str:
        return f"(+ {self.__value})"

class INT():
    """
    Chruch encoding of Numeral
    """
    def __init__(self, function:Callable) -> None:
        self.__lambda=function
    def __call__(self, mapping:Callable, x:Callable=None) -> Any:
        if x is None:
            def inner_int(x):
                return self.__lambda(mapping, x)
            return inner_int
        return self.__lambda(mapping, x)
    def __add__(self, other):
        if isinstance(other, int):
            return int(self)+other
        return PLUS(self,other)
    def __sub__(self, other):
        if isinstance(other, int):
            return int(self)-other
        return MINUS(self,other)
    def __mul__(self, other):
        if isinstance(other, int):
            return int(self)*other
        return TIMES(self, other)
    def __lt__(self, other)->bool:
        return not self.__ge__(other)
    def __le__(self, other)->bool:
        return LE(self, other)(True,False)
    def __gt__(self, other)->bool:
        return not self.__le__(other)
    def __ge__(self, other)->bool:
        return not self.__gt__(other) and self.__eq__(other)
    def __eq__(self, other)->bool:
        return EQ(self, other)(True,False)
    def __int__(self)->int:
        return self(Increment(),0)
    def __str__(self) -> str:
        return f"INT(={int(self)})"



def SUCC(number:INT)->INT:
    """
    Returns the next numeral of the number.
    """
    def inner_succ(f,x):
        return f(number(f,x))
    return INT(inner_succ)

def PLUS(m:INT, n:INT)->INT:
    """
    Adds m to n
    """
    return m(SUCC, n)

def TIMES(m:INT, n:INT)->INT:
    """
    Multiply m and n
    """
    def inner_times(f,x):
        return m(n(f),x)
    return INT(inner_times)

def ISZERO(number:INT)->Bool:
    """
    Check if the number is ZERO
    """
    def inner_iszero(_):
        return F
    return number(inner_iszero, T)

def PRED(number:INT)->INT:
    """
    Returns the previous numeral of the number.\n
    Returns ZERO if the number is ZERO.
    """
    def inner_pred(f,x):
        return number(lambda g: (lambda h:h(g(f))), lambda _:x)( lambda u:u )
    return INT(inner_pred)

def MINUS(m:INT, n:INT)->INT:
    """
    Subtracts n from m.
    Returns ZERO if the answer is less than or equal to ZERO.
    """
    return n(PRED)(m)

def LE(m:INT, n:INT)->Bool:
    """
    Check if m is less than or equal to n
    """
    return ISZERO(MINUS(m,n))

def EQ(m:INT, n:INT)->Bool:
    """
    Check if m is equal to n
    """
    return AND(LE(m,n),LE(n,m))

ZERO=INT(Lambda(lambda _,x:x,"ZERO"))
ONE=INT(Lambda(lambda f,x:f(x),"ONE"))
TWO=SUCC(ONE)
THREE=INT(Lambda(lambda f,x:f(f(f(x))),"THREE"))