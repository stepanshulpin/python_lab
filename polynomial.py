class Polynomial(object):
    def __init__(self, coefficients):
        i = 0
        while i < len(coefficients):
            if coefficients[i]==0:
                coefficients.pop(0)
                i-=1
            elif coefficients[i]!=0:
                break
            i+=1
        self.coefficients = coefficients

    def __str__(self):
        res=""
        i=0
        for c in reversed(self.coefficients):
            if c!=0:
                space = " " if len(res) > 0 else ""
                if i==0:
                    var_in_degree = "" if abs(c) != 1 else "1"
                elif i==1:
                    var_in_degree = "x" +  space
                else:
                    var_in_degree = "x^" + str(i) + space

                if abs(c) != 1:
                    res = str(abs(c)) + var_in_degree + res
                else:
                    res = var_in_degree + res
                if i!=len(self.coefficients)-1:
                    res = sign(c) + " " + res
                elif c<0:
                    res = sign(c) + res
            i+=1
        return res

    def __repr__(self):
        return "Polynomial({})".format(self.coefficients)

    def __add__(self, other):
        c1=self.coefficients
        c2=other.coefficients
        l=max(len(c1),len(c2))
        while len(c1)<l: c1.insert(0,0)
        while len(c2)<l: c2.insert(0,0)
        coefficients = list(map(lambda x,y:x+y, self.coefficients, other.coefficients))
        return Polynomial(list(coefficients))





def sign(i):
    if i>0:
        return "+"
    elif i<0:
        return "-"
