"""
Church encoding of pairs and lists

Author: Minsoo Kim<km19809@users.noreply.github.com>
"""
from typing import Callable
from .boolean import Bool, T, F

def PAIR(first: Callable, second: Callable) -> Callable:
    """
    Makes two input as a pair
    """
    def inner_pair(selector: Callable):
        return selector(first, second)
    return inner_pair


def FIRST(pair: Callable) -> Callable:
    """
    Returns the first item of the pair
    """
    return pair(T)


def SECOND(pair: Callable) -> Callable:
    """
    Returns the second item of the pair
    """
    return pair(F)

def NIL(_):
    """
    Church encoding of NIL(None)
    """
    return T

def NULL(pair:Callable)->Bool:
    """
    Check if the pair is NIL.
    """
    def inner_null(_,__):
        return F
    return pair(inner_null)