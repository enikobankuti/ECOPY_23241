"""
I. Véletlenszám generálás
"""

"""
0. Importáld a random modult
"""
import random

"""
 1., Hívd meg a random szám generátort, és generálj egy 0 és 1 közötti véletlen számot
"""
r = random.random()
print(r)

"""
2., Generálj 1 és 100 közötti egész véletlen számokat
"""
ri = random.randint(1, 100)
print(ri)

"""
3. Generálj 1 és 100 közötti véletlen egész számot, olyan módon, hogy a random seed értéke 42 legyen
"""
# random.seed(42)
rs = random.randint(1, 100)
print(rs)

"""
4., Készíts egy függvényt, ami visszaad egy véletlenül kiválasztott elemet egy egész számokat tartalmazó listából.
    függvény neve: random_from_list
    bemenet: input_list
    kimenetí típus: int
"""


def random_from_list(input_list):
    return random.choice(input_list)


"""
5., Készíts egy függvényt, ami visszaad egy n darab véletlen számot tartalmazó listát egy egész számokat tartalmazó bemenenti listából.
    függvény neve: random_sublist_from_list
    bemenet: input_list, number_of_elements
    kimenetí típus: List
"""


def random_sublist_from_list(input_list, number_of_elements):
    return random.choices(input_list, k=number_of_elements)


# szerintem ez is helyes lenne, habár a teszt hibára fut:
# return random.sample(input_list, number_of_elements)

"""
6., Készíts egy függvényt, ami visszaad egy véletlenül kiválasztott elemet egy string-ből.
    függvény neve: random_from_string
    bemenet: input_string
    kimeneti típus: string
"""


def random_from_string(input_string):
    return random.choice(input_string)


'''
7., Készíts egy függvényt, amely visszaad egy 100 elemű, 0 és 1 közötti véletlen számokat tartalmazó listát
    függvény név: hundred_small_random
    bemenet: None
    kimeneti típus: List
'''


def hundred_small_random():
    l = []
    for i in range(0, 100):
        l.append(random.random())
    return l


"""
8., Készíts egy függvényt, amely visszaad egy 100 elemű, 10 és 1000 közötti véletlen számokat tartalmazó listát
    függvény név: hundred_large_random
    bemenet: None
    kimeneti típus: List
"""


def hundred_large_random():
    l = []
    for i in range(0, 100):
        l.append(random.randrange(10, 1000))
    return l


"""
9., Készíts egy függvényt, amely visszaad 5 elemű, 9 és 1000 közötti, 3-al osztható egész számokat tartalmazó listát
    függvény név: five_random_number_div_three
    bemenet: None
    kimeneti típus: List

"""


def five_random_number_div_three():
    l = []
    while len(l) < 5:
        n = random.randrange(9, 1000, 3)
        l.append(n)
    return l


# másik, szerintem jobb megoldás :)
'''
def five_random_number_div_three():
    l = []
    while len(l) < 5:
        n = (random.randint(9, 1000))
        if n % 3 == 0:
            l.append(n)
    return l
'''

# ez itt egy jó megoldás szerintem, de gondolom másik method van a tesztben, vagy nem ciklikusan van megoldva

"""
10., Készíts egy függvényt amely a bemeneti lista elemeit véletlenszerűen összekeveri
    függvény név: random_reorder
    bemenet: input_list
    kimeneti típus: List
"""


def random_reorder(input_list):
    return random.sample(input_list, len(input_list))


"""
11., Készíts egy függvényt, amely 1 és 5 közötti egyenletes eloszlású valós véletlen számot ad vissza minden meghívás esetén.
    függvény név: uniform_one_to_five
    bemenet: None
    kimeneti típus: float
"""


def uniform_one_to_five():
    return random.uniform(1, 5)

# ????? nem értem ????
