class Polynomial(object):
    @property
    def coeffs(self):
        return self._coeffs

    def __init__(self, coeffs):
        if isinstance(coeffs, Polynomial):
            coeffs=coeffs.coeffs
        if isinstance(coeffs, (tuple,)):
            coeffs = list(coeffs)
        self.coeffs = coeffs

    @coeffs.setter
    def coeffs(self,coeffs):
        if isinstance(coeffs, (list,)):
            i = 0
            while i < len(coeffs):
                if coeffs[i] == 0:
                    coeffs.pop(0)
                    i -= 1
                elif coeffs[i] != 0:
                    break
                i += 1
            self._coeffs = coeffs
        else:
            raise TypeError

    @coeffs.getter
    def coeffs(self):
        return self._coeffs

    def __str__(self):
        res = ""
        i = 0
        if len(self.coeffs) == 0:
            res = "0"
        else:
            for c in reversed(self.coeffs):
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
                    if i != len(self.coeffs) - 1:
                        res = sign(c) + " " + res
                    elif c < 0:
                        res = sign(c) + res
                i += 1
        return res

    def __repr__(self):
        return "Polynomial({})".format(self.coeffs)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.coeffs
            c2 = other.coeffs
            l = max(len(c1), len(c2))
            while len(c1) < l: c1.insert(0, 0)
            while len(c2) < l: c2.insert(0, 0)
            coeffs = list(map(lambda x, y: x + y, self.coeffs, other.coeffs))
            return Polynomial(coeffs)
        if isinstance(other, int):
            c = self.coeffs
            c[len(c) - 1] += other
            return Polynomial(list(c))
        raise TypeError

    def __radd__(self, other):
        if isinstance(other, int):
            return self + other
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.coeffs
            c2 = other.coeffs
            l = max(len(c1), len(c2))
            while len(c1) < l: c1.insert(0, 0)
            while len(c2) < l: c2.insert(0, 0)
            coeffs = list(map(lambda x, y: x - y, self.coeffs, other.coeffs))
            return Polynomial(coeffs)
        if isinstance(other, int):
            c = self.coeffs
            c[len(c) - 1] -= other
            return Polynomial(list(c))
        raise TypeError

    def __rsub__(self, other):
        if isinstance(other, int):
            c = list(map(lambda x: (-1) * x, self.coeffs))
            free_member = other + c[len(c) - 1]
            c[len(c) - 1] = free_member
            return Polynomial(c)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            c = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
            for i1, c1 in enumerate(self.coeffs):
                for i2, c2 in enumerate(other.coeffs):
                    c[i1 + i2] += c1 * c2
            return Polynomial(c)
        if isinstance(other, int):
            return Polynomial(list(map(lambda x: other * x, self.coeffs)))
        raise TypeError

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeffs) == len(other.coeffs):
                return self.coeffs < other.coeffs
            else:
                return len(self.coeffs) < len(other.coeffs)
        raise TypeError("'<' not supported between these instance")

    def __le__(self, other):
        if isinstance(other, Polynomial):
            return self.__lt__(other) or self == other
        raise TypeError("'<' not supported between these instance")

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, Polynomial):
            return not self.__le__(other)
        raise TypeError("'>' not supported between these instance")

    def __ge__(self, other):
        if isinstance(other, Polynomial):
            return not self.__lt__(other)
        raise TypeError("'>=' not supported between these instance")


def sign(i):
    if i > 0:
        return "+"
    elif i < 0:
        return "-"
