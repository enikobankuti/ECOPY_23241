# Lista feladatok

# 1., Hozzon létre egy listát a következő elemekkel a Subscript operátor segítségével: 17, 18, 3.14, a, alma

a = [17, 18, 3.14, "a", "alma"]

# 2., Hozzon létre egy listát a list() függvény alkalmazásával: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

b: list() = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 3., Adja vissza a lista 1. indexén lévő elemét

var = b[1]

# 4., Adja vissza a lista 1 elemét

var1 = b[0]  # első elemét?

# 5., Adja vissza a lista legnagyobb elemét

m = max(b)

# 6. Adja vissza a lista legnagyobb elemének az indexét

x = b.index(max(b))


# 7., Írjon egy függvényt ami megvizsgálja, hogy a listában létezik-e egy adott elem
# függvény név: contains_value
# bemeneti paraméterek: input_list, element
# kimeneti típus: bool

def contains_value(input_list, element):
    if element in input_list:
        return True
    else:
        return False


# 8., Írjon egy függvényt ami megvizsgálja, hogy hány elem található a listában.
# függvény név: number_of_elements_in_list
# bemeneti paraméterek: input_list
# kimeneti típus: int
def number_of_elements_in_list(input_list):
    return len(input_list)


# 9., Írjon egy függvényt ami törli az összes elemet a listából
# függvény név: remove_every_element_from_list
# bemeneti paraméterek: input_list
# kimeneti típus: None

def remove_every_element_from_list(input_list):
    input_list.clear()


# 10., Írjon egy függvényt ami fordított sorrendben adja vissza a lista összes elemét
# függvény név: reverse_list
# bemeneti paraméterek: input_list
# kimeneti típus: List

def reverse_list(input_list):
    input_list.reverse()
    return input_list


# 11., Írjon egy függvényt ami vissza adja a bemeneti lista páratlan elemeit
# függvény név: odds_from_list
# bemeneti paraméterek: input_list
# kimeneti típus: List

def odds_from_list(input_list):
    odds = list()
    for i in input_list:
        if i % 2 == 1:
            odds.append(i)
    return odds


# 12., Írjon egy függvényt ami megszámolja a bemeneti lista páratlan elemeit
# függvény név: number_of_odds_in_list
# bemeneti paraméterek: input_list
# kimeneti típus: int

def number_of_odds_in_list(input_list):
    count = 0
    for i in input_list:
        if i % 2 == 1:
            count += 1
    return count


# 13., Írjon egy függvényt ami visszaadja, hogy a bemeneti listának van-e páratlan eleme
# függvény név: contains_odd
# bemeneti paraméterek: input_list
# kimeneti típus: bool

def contains_odd(input_list):
    cont_odd = False
    for i in input_list:
        if i % 2 == 1:
            cont_odd = True
            break
    return cont_odd


# 14., Írjon egy függvényt ami visszaadja a 2. legnagyobb elemet listában
# függvény név: second_largest_in_list
# bemeneti paraméterek: input_list
# kimeneti típus: int

def second_largest_in_list(input_list):
    list1 = sorted(input_list)
    return list1[-2]


# 15., Írjon egy függvényt ami kiszámítja a lista elemek összegét
# függvény név: sum_of_elements_in_list
# bemeneti paraméterek: input_list
# kimeneti típus: float

def sum_of_elements_in_list(input_list):
    sum: float = 0
    for i in input_list:
        sum += i
    return sum


# 16., Írjon egy függvényt ami kiszámítja a lista elemek kumulált összegét
# függvény név: cumsum_list
# bemeneti paraméterek: input_list
# kimeneti típus: List

def cumsum_list(input_list):
    new = []
    sum = 0
    for i in range(0, len(input_list)):
        sum += input_list[i]
        new.append(sum)
    return new


# 17., Írjon egy függvényt ami kiszámítja 2 lista elemenként vett összegét
# függvény név: element_wise_sum
# bemeneti paraméterek: input_list1, input_list2
# kimeneti típus: List

def element_wise_sum(input_list1, input_list2):
    list3 = []
    if len(input_list1) == len(input_list2):
        for i in range(0, len(input_list1)):
            list3.append(input_list1[i] + input_list2[i])
    return list3


# 18., Írjon egy függvényt ami visszaadja egy lista, 2 tetszőleges index között vett rész listáját
# függvény név: subset_of_list
# bemeneti paraméterek: input_list, start_index, end_index
# kimeneti típus: List

def subset_of_list(input_list, start_index, end_index):
    return input_list[start_index:end_index + 1]


# 19., Írjon egy függvényt ami visszaadja egy lista minden n-edik elemét listaként
# függvény név: every_nth
# bemeneti paraméterek: input_list, step_size
# kimeneti típus: List

def every_nth(input_list, step_size):
    return input_list[::step_size]


# 20., Írjon egy függvényt ami eldönti, hogy a lista minden eleme egyedi-e
# függvény név: only_unique_in_list
# bemeneti paraméterek: input_list
# kimeneti típus: bool

def only_unique_in_list(input_list):
    unique = True
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if i != j & input_list[i] == input_list[j]:
                unique = False
                break

    return unique


# 21., Írjon egy függvényt amely eltávolítja a duplikált lista elemeket
# függvény név: keep_unique
# bemeneti paraméterek: input_list
# kimeneti típus: List

def keep_unique(input_list):
    list2 = []
    for i in input_list:
        if i not in list2:
            list2.append(i)
    return list2


# 22., Írjon egy függvényt amely kicserél 2 tetszőleges elemet a listában
# függvény név: swap
# bemeneti paraméterek: input_list, first_index, second_index
# kimeneti típus: List

def swap(input_list, first_index, second_index):
    temp = input_list[first_index]
    input_list[first_index] = input_list[second_index]
    input_list[second_index] = temp
    return input_list


# 23., Írjon egy függvényt amely töröl egy megadott elemet a listából
# függvény név: remove_element_by_value
# bemeneti paraméterek: input_list, value_to_remove
# kimeneti típus: List

def remove_element_by_value(input_list, value_to_remove):
    for i in input_list:
        if input_list[i] == value_to_remove:
            input_list.remove(value_to_remove)  # ?????????????????????
            break
    return input_list


# 24., Írjon egy függvényt amely töröl egy megadott indexű elemet a listából
# függvény név: remove_element_by_index
# bemeneti paraméterek: input_list, index
# kimeneti típus: List

def remove_element_by_index(input_list, index):
    input_list.remove(input_list[index])
    return input_list


# 25., Írjon egy függvényt amely egy tetszőleges számmal megszorozza a lista összes elemét
# függvény név: multiply_every_element
# bemeneti paraméterek: input_list, multiplier
# kimeneti típus: List

def multiply_every_element(input_list, multiplier):
    for i in range(0, len(input_list)):
        input_list[i] *= multiplier
    return input_list


# Dictionary feladatok
# %%
# 1. Hozz létre egy dictionary-t (dict.) amelyhez a két kulcs 'a' és 'b' és a hozzájuk tartozó értékek rendre 9 és [12, 'c']

dicti = {'a': 9, 'b': [12, 'c']}

# 2. Kérd le az előző dictionary 'a' kulcsán lévő értéket

print(dicti['a'])

# 3. Kérd le az előző dictionary 'd' kulcsán lévő értéket olyan módon, hogy ne hibát kapj, hanem Null legyen a visszatérési érték
#
print(dicti.get('d'))


# 4., Írjon egy függvényt amely töröl egy megadott kulcsú elemet a dict.-ből
# függvény név: remove_key
# bemeneti paraméterek: input_dict, key
# kimeneti típus: Dict

def remove_key(input_dict, key):
    input_dict.pop(key, 'no key')
    return input_dict


# 5., Írjon egy függvényt amely a sorba rendezi a kulcs-érték párokat a kulcs értéke szerint egy dictionary-ben
# függvény név: sort_by_key
# bemeneti paraméterek: input_dict
# kimeneti típus: Dict


from collections import OrderedDict


def sort_by_key(input_dict):
    input_dict = OrderedDict(sorted(input_dict.items()))
    return input_dict


# 6., Írjon egy függvényt amely összeadja a dict.-ben található összes értéket
# függvény név: sum_in_dict
# bemeneti paraméterek: input_dict
# kimeneti típus: float

def sum_in_dict(input_dict):
    return sum(input_dict.values())


# 7., Írjon egy függvényt amely összekapcsol 2 dictionary-t 1 dict.-ben
# függvény név: merge_two_dicts
# bemeneti paraméterek: input_dict1, input_dict2
# kimeneti típus: Dict

def merge_two_dicts(input_dict1, input_dict2):
    input_dict1.update(input_dict2)
    return input_dict1


# 8., Írjon egy függvényt amely összekapcsol n dictionary-t 1 dict.-ben
# függvény név: merge_dicts
# bemeneti paraméterek: *dicts
# kimeneti típus: Dict

def merge_dicts(*dicts):  # ?????????????????????????????????????????
    return dicts


# 9., Írjon egy függvényt amely a bemeneti, pozitív egész számokat tartalmazó listát kiválogatja páros és páratlan számokra, és visszaad egy olyan dictionary-t, amelyben a kulcs az 'even' és 'odd', az értékek, pedig a listák.
# függvény név: sort_list_by_parity
# bemeneti paraméterek: input_list
# kimeneti típus: Dict

def sort_list_by_parity(input_list):
    even = []
    odd = []
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return {'even': even, 'odd': odd}


# 10., Írjon egy függvényt amely a bemenetként kapott dictionary értékeinél található listák átlagait adja vissza egy új dictionary-be. {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....} -> {"some_key":mean_of_values,"another_key":mean_of_values,....}
# függvény név: mean_by_key_value
# bemeneti paraméterek: input_dict
# kimeneti típus: Dict

def mean_by_key_value(input_dict):
    for i in input_dict:
        input_dict[i] = sum(input_dict[i]) / len(input_dict[i])
    return input_dict


# 11., Írjon egy függvényt amely a bemeneti lista értékeinek előállítja a gyakoriságát
# függvény név: count_frequency
# bemeneti paraméterek: input_list
# kimeneti típus: Dict

def count_frequency(input_list):
    d = {}
    for i in input_list:
        print(i)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
