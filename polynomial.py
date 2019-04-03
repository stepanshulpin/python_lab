class Polynomial(object):
    def __init__(self, coefficients):
        if isinstance(coefficients, (list,)):
            i = 0
            while i < len(coefficients):
                if coefficients[i] == 0:
                    coefficients.pop(0)
                    i -= 1
                elif coefficients[i] != 0:
                    break
                i += 1
            if len(coefficients) != 0:
                self.coefficients = coefficients
            else:
                raise ValueError
        else:
            raise TypeError

    def __str__(self):
        res = ""
        i = 0
        for c in reversed(self.coefficients):
            if c != 0:
                space = " " if len(res) > 0 else ""
                if i == 0:
                    var_in_degree = "" if abs(c) != 1 else "1"
                elif i == 1:
                    var_in_degree = "x" + space
                else:
                    var_in_degree = "x^" + str(i) + space

                if abs(c) != 1:
                    res = str(abs(c)) + var_in_degree + res
                else:
                    res = var_in_degree + res
                if i != len(self.coefficients) - 1:
                    res = sign(c) + " " + res
                elif c < 0:
                    res = sign(c) + res
            i += 1
        return res

    def __repr__(self):
        return "Polynomial({})".format(self.coefficients)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.coefficients
            c2 = other.coefficients
            l = max(len(c1), len(c2))
            while len(c1) < l: c1.insert(0, 0)
            while len(c2) < l: c2.insert(0, 0)
            coefficients = list(map(lambda x, y: x + y, self.coefficients, other.coefficients))
            return Polynomial(coefficients)
        if isinstance(other, int):
            c = self.coefficients
            c[len(c) - 1] += other
            return Polynomial(list(c))
        raise TypeError

    def __radd__(self, other):
        if isinstance(other, int):
            return self + other
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.coefficients
            c2 = other.coefficients
            l = max(len(c1), len(c2))
            while len(c1) < l: c1.insert(0, 0)
            while len(c2) < l: c2.insert(0, 0)
            coefficients = list(map(lambda x, y: x - y, self.coefficients, other.coefficients))
            return Polynomial(coefficients)
        if isinstance(other, int):
            c = self.coefficients
            c[len(c) - 1] -= other
            return Polynomial(list(c))
        raise TypeError

    def __rsub__(self, other):
        if isinstance(other, int):
            c = list(map(lambda x: (-1) * x, self.coefficients))
            free_member = other + c[len(c) - 1]
            c[len(c) - 1] = free_member
            return Polynomial(c)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            c = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i1, c1 in enumerate(self.coefficients):
                for i2, c2 in enumerate(other.coefficients):
                    c[i1 + i2] += c1 * c2
            return Polynomial(c)
        if isinstance(other, int):
            return Polynomial(list(map(lambda x: other * x, self.coefficients)))
        raise TypeError

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coefficients) == len(other.coefficients):
                return self.coefficients < other.coefficients
            else:
                return len(self.coefficients) < len(other.coefficients)
        raise TypeError

    def __le__(self, other):
        if isinstance(other, Polynomial):
            return self.__lt__(other) or self == other
        raise TypeError

    def __ne__(self, other):
        if isinstance(other, Polynomial):
            return self.coefficients != other.coefficients
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, Polynomial):
            return not self.__le__(other)
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, Polynomial):
            return not self.__lt__(other)
        raise TypeError


def sign(i):
    if i > 0:
        return "+"
    elif i < 0:
        return "-"
