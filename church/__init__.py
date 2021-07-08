"""
Simple Church encoding implmentations.

Author: Minsoo Kim<km19809@users.noreply.github.com>
"""
from typing import Callable
from .boolean import T, F, AND, OR, NOT, XOR, IF
from .numeral import Increment, SUCC, PLUS, TIMES, ISZERO, ZERO, ONE, TWO, THREE
from .pair import PAIR, FIRST, SECOND, NULL, NIL
if __name__=="__main__":
    #===bool===
    for op1 in [T, F]:
        for op2 in [T, F]:
            print(f"For {op1} and {op2}:")
            print(f"\tAND: {AND(op1,op2)}")
            print(f"\tOR: {OR(op1,op2)}")
            print(f"\tNOT: {NOT(op1)}, {NOT(op2)}")
            print(f"\tXOR: {XOR(op1,op2)}")
    #===numbers===
    print(TWO(Increment(),Increment(0)))
    FIVE=PLUS(TWO, SUCC(TWO))
    print(FIVE(Increment(),Increment(0)))
    SIX=TIMES(THREE, TWO)
    print(SIX(Increment(),Increment(0)))
    print(ISZERO(ZERO))
    print(THREE+SIX)
    print(TWO-ONE)
    print(ONE-TWO)
    print(THREE<=SIX)
    print((THREE*FIVE)>=SIX)
    print(THREE==SIX)
    print(THREE*5)
    #===list===
    FOUR=TWO+TWO
    _list=PAIR(FOUR,PAIR(THREE,PAIR(TWO,PAIR(ONE, PAIR(ZERO,NIL)))))

    def trace(li:Callable):
        print(FIRST(li), end=', ')
        (IF(NULL(SECOND(li)), NIL, trace))(SECOND(li))

    trace(_list)