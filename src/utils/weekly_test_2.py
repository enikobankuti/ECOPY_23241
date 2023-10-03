"""
1., Hozzan létre egy új osztályt aminek a neve LaplaceDistribution. Definiáljon benne a __init__ nevű függvényt,
amelynek bemenetként kap egy véletlenszám generátort, és az eloszlás várható értékét (location) és
varianciáját (scale), amely értékeket adattagokba ment le.
    Osztály név: LaplaceDistribution
    függvény név: __init__
    bemenet: self, rand, loc, scale
    link: https://en.wikipedia.org/wiki/Laplace_distribution

"""
import math
import random
from src.utils import helper


class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        pdf = 1 / (2 * self.scale) * math.exp(-(abs(x - self.loc) / self.scale))
        return pdf

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        return self.loc - self.scale * helper.sign(p - 0.5) * math.log(1 - 2 * abs(p - 0.5))

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.loc

    def variance(self):
        return 2 * self.scale ** 2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 3

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


"""
2., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely loc várható értékű, scale varianciájú és
asymmmetry ferdeségű  aszimmetrikus laplace eloszlás eloszlásfüggvényéből rendel valószínűségi értéket a
bemeneti x valós számhoz.
    függvény név: pdf
    bemenet: x
    kimeneti típus: float

3., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely megvalósítja az eloszlás kumulatív eloszlás függvényét.
    függvény név: cdf
    bemenet: x
    kimeneti típus: float

4., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely implementálja az eloszlás inverz kumulatív eloszlás függvényét
    függvény név: ppf
    bemenet: p
    kimeneti típus: float

5., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely az osztály létrehozásánál megadott paraméterek mellett, 
aszimmetrikus laplace eloszlású véletlen számokat generál minden meghívásnál
    függvény név: gen_random
    bemenet: None
    kimeneti típus: float

6., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény várható értékét. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment     undefined") parancsot.
    függvény név: mean
    bemenet: None
    kimeneti típus: float

7., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény varianciáját. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment        undefined") parancsot.
    függvény név: variance
    bemenet: None
    kimeneti típus: float

8., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény ferdeségét. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment          undefined") parancsot.
    függvény név: skewness
    bemenet: None
    kimeneti típus: float

9., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény többlet csúcsosságát. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception        ("Moment undefined") parancsot.
    függvény név: ex_kurtosis
    bemenet: None
    kimeneti típus: float

10., Egészítse ki a LaplaceDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény első momentumát, a 2. és 3. cetrális momentumát, és a többlet csúcsosságot.. Ha az eloszlásnak nincsenek ilyen       értékei, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mvsk
    bemenet: None
    kimeneti típus: List
"""


class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x < 1:
            return 0
        else:
            return (self.shape * (self.scale ** self.shape)) / (x ** (self.shape + 1))

    def cdf(self, x):
        if x < self.scale:
            return 0
        else:
            return 1 - (self.scale / x) ** self.shape

    def ppf(self, p):
        return self.scale * (1 - p) ** (-1 / self.shape)

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        if self.shape <= 1:
            return float('inf')
        else:
            return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            return float('inf')
        else:
            return (self.scale ** 2 * self.shape) / ((self.shape - 1) ** 2 * (self.shape - 2))

    def skewness(self):
        if self.shape > 3:
            return (2 * (1 + self.shape)) / (self.shape - 3) * math.sqrt((self.shape - 2) / self.shape)
        elif self.shape <= 1:
            raise Exception("Moment undefined")
        else:
            return math.inf

    def ex_kurtosis(self):
        if self.shape > 4:
            return (6 * ((self.shape ** 3) + (self.shape ** 2) - (6 * self.shape) - 2)) / (self.shape * (self.shape-3) * (self.shape - 4))
        elif self.shape <= 1:
            raise Exception("Moment undefined")
        else:
            return math.inf

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


"""
11., Hozzan létre egy új osztályt aminek a neve ParetoDistribution. Definiáljon benne a __init__ nevű függvényt, amelynek bemenetként kap egy véletlenszám generátort, és az eloszlás skála paraméterét (scale) és alak         paraméterét (shape), amely értékeket adattagokba ment le.
    Osztály név: ParetoDistribution
    függvény név: __init__
    bemenet: self, rand, scale, shape
    link: https://en.wikipedia.org/wiki/Pareto_distribution
    help: https://www.wolframalpha.com/input?i=pareto+distribution+k%3D1+alpha+%3D+2.1

12., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely loc várható értékű, scale varianciájú és asymmmetry ferdeségű  aszimmetrikus laplace eloszlás eloszlásfüggvényéből rendel valószínűségi értéket a     bemeneti x valós számhoz.
    függvény név: pdf
    bemenet: x
    kimeneti típus: float

13., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely megvalósítja az eloszlás kumulatív eloszlás függvényét.
    függvény név: cdf
    bemenet: x
    kimeneti típus: float

14., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely implementálja az eloszlás inverz kumulatív eloszlás függvényét
    függvény név: ppf
    bemenet: p
    kimeneti típus: float

15., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely az osztály létrehozásánál megadott paraméterek mellett, aszimmetrikus laplace eloszlású véletlen számokat generál minden meghívásnál
    függvény név: gen_random
    bemenet: None
    kimeneti típus: float


16., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény várható értékét. Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment     undefined") parancsot.
    függvény név: mean
    bemenet: None
    kimeneti típus: float

17., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény varianciáját.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment       undefined") parancsot.
    függvény név: variance
    bemenet: None
    kimeneti típus: float

18., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény ferdeségét.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception("Moment         undefined") parancsot.
    függvény név: skewness
    bemenet: None
    kimeneti típus: float

19., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény többlet csúcsosságát.  Ha az eloszlásnak nincsen ilyen értéke, akkor return helyett hívja meg a raise Exception       ("Moment undefined") parancsot.
    függvény név: ex_kurtosis
    bemenet: None
    kimeneti típus: float

20., Egészítse ki a ParetoDistribution osztályt egy új függvénnyel, amely visszaadja az eloszlás függvény első momentumát, a 2. és 3. cetrális momentumát, és a többlet csúcsosságot.  Ha az eloszlásnak nincsenek ilyen        értékei, akkor return helyett hívja meg a raise Exception("Moment undefined") parancsot.
    függvény név: mvsk
    bemenet: None
    kimeneti típus: List
"""
