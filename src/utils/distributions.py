#### II. Eloszlások ####


"""
1., Hozz létre egy új osztályt, aminek a neve FirstClass
    osztály név: FirstClass
"""

import random
import math
from pyerf import pyerf


class FirstClass:
    pass


"""
2., Hozz létre egy új osztályt, aminek a neve SecondClass, és definiáljon benne egy __init__ nevű függvényt, 
amely bead egy véletlenszám generátort a self.random adattagnak.
    Osztály név: SecondClass
    függvény név: __init__
    bemenet: self, rand
"""


class SecondClass:

    def __init__(self, rand):
        self.random = rand


# v = SecondClass(random)
# print(v.random.random())

"""
3., Hozzan létre egy új osztályt aminek a neve UniformDistribution. Definiáljon benne a __init__ nevű függvényt, 
amelynek bemenetként kap egy véletlenszám generátort, és az eloszlás alsó (a) és felső határát (b), amely értékeket adattagokba ment le.
    Osztály név: UniformDistribution
    függvény név: __init__
    bemenet: self, rand, a, b
"""

"""
4., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely a és b pont közötti értékekhez a hozzájuk 
tartozó egyenletes eloszlás, eloszlás függvényében hozzárendelt értékét rendeli.
    függvény név: pdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
5., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely megvalósítja az egyenletes eloszlás kumulatív 
eloszlás függvényét.
    függvény név: cdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
6., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely implementálja az egyenletes eloszlás inverz 
kumulatív eloszlás függvényét. (percent-point function)
    függvény név: ppf
    bemenet: p
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
7., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely az osztály létrehozásánál megadott paraméterek 
mellett, egyenletes eloszlású véletlen számokat generál minden meghívásnál.
    függvény név: gen_random
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""


class UniformDistribution:
    def __init__(self, rand, a, b):
        self.x = None
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if x < self.a or x > self.b:
            pdf = 0.0
        else:
            pdf = 1.0 / (self.b - self.a)
        return pdf

    def cdf(self, x):
        if x < self.a:
            cdf = 0.0
        elif x > self.b:
            cdf = 1.0
        else:
            cdf = (x - self.a) / (self.b - self.a)
        return cdf

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Percentile p must be between 0 and 1.")
        ppf = self.a + p * (self.b - self.a)
        return ppf

    def gen_random(self):
        return random.uniform(self.a, self.b)

    def mean(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        else:
            return (self.a + self.b) / 2

    def median(self):
        return (self.a + self.b) / 2

    def variance(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        else:
            return (self.b - self.a) / 12

    def skewness(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        return 0

    def ex_curtois(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        return -1.2

    def mvsk(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        else:
            l = [self.mean(), self.variance(), self.skewness(), self.ex_curtois()]
            return l


"""
8., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény átlagát.  
Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mean
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
9., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény mediánját.
    függvény név: median
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""
"""
10., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény varianciáját.  
Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: variance
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
11., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény ferdeségét.  
Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: skewness
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""
"""
12., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény többlet csúcsosságát. 
 Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: ex_kurtosis
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""
"""
13., Egészítse ki a UniformDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény első 3 
cetrális momentumát és a többlet csúcsosságot.  Ha az eloszlásnak nincsenek ilyen értékei, akkor return helyett hívja meg 
a raise Exception("Moments undefined") parancsot.
    függvény név: mvsk
    bemenet: None
    kimeneti típus: List
    link: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
"""

"""
14., Hozzan létre egy új osztályt aminek a neve NormalDistribution. Definiáljon benne a __init__ nevű függvényt, 
amelynek bemenetként kap egy véletlenszám generátort, és az eloszlás várható értékét (location) és varianciáját (scale), 
amely értékeket adattagokba ment le.
    Osztály név: NormalDistribution
    függvény név: __init__
    bemenet: self, rand, loc, scale
"""

class NormalDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return ((1 / (self.scale ** 0.5 * ((2 * math.pi) ** 0.5))) *
                (math.e ** (-0.5 * (((x - self.loc) / self.scale ** 0.5) ** 2))))

    def cdf(self, x):
        return (1.0 + math.erf((x - self.loc) / (self.scale ** 0.5 * (2 ** 0.5)))) / 2.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Percentile p must be between 0 and 1.")
        else:
            return self.loc + self.scale ** 0.5 * (2 ** 0.5) * pyerf.erfinv(2 * p - 1)

    def gen_random(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
        return self.scale

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 0

    def mvsk(self):
        l = [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
        return l


"""
15., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely loc várható értékű és scale varianciájú
normális eloszlás eloszlásfüggvényéből rendel valószínűségi értéket a bemeneti x valós számhoz.
    függvény név: pdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
16., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely megvalósítja az eloszlás kumulatív eloszlás függvényét.
    függvény név: cdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
17., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely implementálja az eloszlás inverz kumulatív eloszlás függvényét
    függvény név: ppf
    bemenet: p
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
18., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely az osztály létrehozásánál megadott paraméterek mellett, normális eloszlású véletlen számokat generál minden meghívásnál
    függvény név: gen_random
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution

"""
"""
19., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény átlagát.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mean
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
20., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény mediánját
    függvény név: median
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
21., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény varianciáját.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: variance
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""
"""
22., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény ferdeségét.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: skewness
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""

"""
23., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény többlet csúcsosságát.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: ex_kurtosis
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""

"""
24., Egészítse ki a NormalDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény első 3 cetrális momentumát és a többlet csúcsosságot.  Ha az eloszlásnak nincsenek ilyen értékei, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mvsk
    bemenet: None
    kimeneti típus: List
    link: https://en.wikipedia.org/wiki/Normal_distribution
"""


class CauchyDistribution:
    def __init__(self, rand, x0, gamma):
        self.rand = rand
        self.loc = x0
        self.scale = gamma

    def pdf(self, x):
        return 1 / (math.pi * self.scale * (1 + ((x - self.loc) / self.scale) ** 2))

    def cdf(self, x):
        return 0.5 + (1 / math.pi) * math.atan((x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Percentile p must be between 0 and 1.")
        else:
            return self.loc + self.scale * math.tan(math.pi * (p - 0.5))

    def gen_rand(self):
        return self.loc + self.scale * math.tan(math.pi * (self.rand.random() - 0.5))

    def mean(self):
        raise Exception("Moment undefined")

    def median(self):
        return self.loc

    def variance(self):
        raise Exception("Moment undefined")

    def skewness(self):
        raise Exception("Moment undefined")

    def ex_kurtosis(self):
        raise Exception("Moment undefined")

    def mvsk(self):
        raise Exception("Moments undefined")


"""
25., Hozzan létre egy új osztályt aminek a neve CauchyDistribution. Definiáljon benne a __init__ nevű függvényt, amelynek bemenetként kap egy véletlenszám generátort, az x0 (location) és gamma (scale) értékeket, amelyeket adattagokba ment le.
    Osztály név: CauchyDistribution
    függvény név: __init__
    bemenet: self, rand, loc, scale
"""

"""
26., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely a bemeneti x értékhez hozzárendeli annak valószínűségi értékét
    függvény név: pdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
27., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely megvalósítja az eloszlás kumulatív eloszlás függvényét.
    függvény név: cdf
    bemenet: x
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
28., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely implementálja az eloszlás inverz kumulatív eloszlás függvényét
    függvény név: ppf
    bemenet: p
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
29., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely az osztály létrehozásánál megadott paraméterek mellett, cauchy eloszlású véletlen számokat generál minden meghívásnál
    függvény név: gen_random
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
30., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény átlagát. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mean
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
31., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény mediánját.
    függvény név: median
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
32., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény varianciáját.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: variance
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
33., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény ferdeségét.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: skewness
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
34., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény többlet csúcsosságát.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: ex_kurtosis
    bemenet: None
    kimeneti típus: float
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""

"""
35., Egészítse ki a CauchyDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény első 3 cetrális momentumát és a többlet csúcsosságot.  Ha az eloszlásnak nincsenek ilyen értékei, akkor return helyett hívja meg a raise Exception("Moments undefined") parancsot.
    függvény név: mvsk
    bemenet: None
    kimeneti típus: List
    link: https://en.wikipedia.org/wiki/Cauchy_distribution
"""
