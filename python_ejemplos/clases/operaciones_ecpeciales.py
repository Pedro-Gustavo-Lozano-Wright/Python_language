def operaciones_ecpeciales():
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return "({0},{1})".format(self.x, self.y)

        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)

        def __lt__(self, other):
            self_mag = (self.x ** 2) + (self.y ** 2)
            other_mag = (other.x ** 2) + (other.y ** 2)
            return self_mag < other_mag

    p1 = Point(1, 2)
    p2 = Point(2, 3)

    print(p1 + p2)

    p1 = Point(1, 1)
    p2 = Point(-2, -3)
    p3 = Point(1, -1)

    # use less than
    print(p1 < p2)
    print(p2 < p3)
    print(p1 < p3)

'''
al hacer operacioner aritmeticas con los objetos

Adición	           p1 + p2	p1.__add__(p2)
Sustracción	       p1 - p2	p1.__sub__(p2)
Multiplicación	   p1 * p2	p1.__mul__(p2)
Energía	           p1 ** p2	p1.__pow__(p2)
División	       p1 / p2	p1.__truediv__(p2)
División de piso   p1 // p2	p1.__floordiv__(p2)
Resto (módulo)	   p1 % p2	p1.__mod__(p2)
izquierda bit      p1 << p2	p1.__lshift__(p2)
derecha bit 	   p1 >> p2	p1.__rshift__(p2)
Y bit a bit	       p1 & p2	p1.__and__(p2)
O bit a bit	       p1 | p2	p1.__or__(p2)
XOR bit a bit	   p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	      ~p1	p1.__invert__()


Menos que	      p1 < p2	p1.__lt__(p2)
Menos o igual  	  p1 <= p2	p1.__le__(p2)
Igual a	          p1 == p2	p1.__eq__(p2)
No igual a	      p1 != p2	p1.__ne__(p2)
Mas grande que	  p1 > p2	p1.__gt__(p2)
Mayor o igual 	  p1 >= p2	p1.__ge__(p2)

'''