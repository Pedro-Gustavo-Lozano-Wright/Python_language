from fractions import Fraction as F
import fractions
import math

#https://www.programiz.com/python-programming/modules/math


def matematicas_general():

    print(fractions.Fraction(1.5))
    print(fractions.Fraction(5))
    print(fractions.Fraction(1, 3))
    print(F(1, 3) + F(1, 3))
    print(1 / F(5, 6))
    print(F(-3, 10) > 0)
    print(F(-3, 10) < 0)

    print(math.pi)
    print(math.cos(math.pi))
    print(math.exp(10))
    print(math.log10(1000))
    print(math.sinh(1))
    print(math.factorial(6))

    print("math.floor(-23.11) : ", math.floor(-23.11))
    print("math.floor(300.16) : ", math.floor(300.16))

    print("math.ceil(-23.11) : ", math.ceil(-23.11))
    print("math.ceil(300.16) : ", math.ceil(300.16))

    list_num = [3, 9, 7, 4]
    print(sum(list_num))