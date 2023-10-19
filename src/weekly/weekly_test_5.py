from pathlib import Path

file_to_load = Path.cwd().parent.joinpath('data').joinpath('chipotle.tsv')

import pandas as pd
import matplotlib as plt
import random as rand
import typing as tp

"""
1., Olvasd be a data mappa chipotle.tsv nevű fájlját egy dataframe-be. A betöltött   adatokat food nevű változóban mentse. 
A következő feladatokban a kiinduló fájlt csak akkor írd felül, ha jelezve van.
"""
food = pd.read_csv('/Users/Enci/Documents/GitHub/ECOPY_23241/data/chipotle.tsv', sep='\t')

"""
2., Készts egy függvényt, ami a bemeneti adattömbben átalakítja az item_price értékeit float-ra. 
Az eredeti adatokat a függvény ne módosítsa. A kapott, tisztított adatokkal írd felül a food változót.

függvény név: change_price_to_float
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


def change_price_to_float(input_df):
    input_df['item_price'] = input_df['item_price'].str.replace('$', '').astype(float)
    return input_df


"""
3., Készíts egy függvényt, ami megmondja, hogy hány megfigyelés található az adathalmazban

függvény név: number_of_observations
bemenet: input_df
kimeneti típus: int
"""


def number_of_observations(input_df):
    return len(input_df.index)


"""
4., Készíts egy függvényt, ami visszadja a termék neveket és az áraikat.

függvény név: items_and_prices
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


def items_and_prices(input_df):
    return change_price_to_float(food[['item_name', 'item_price']])


"""
5., Készíts egy függvényt, ami sorba rendezi az termékeket az áruk alapján, csökkenő sorrendben. Használd az előző  függvény eredményét.

függvény név: sorted_by_price
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


def sorted_by_price(input_df):
    return items_and_prices(input_df).sort_values(by=['item_price'], ascending=False)


"""
6., Készíts egy függvényt, ami visszaadja az átlagos árat.

függvény név: avg_price
bemenet: input_df
kimeneti típus: float
"""


def avg_price(input_df):
    return input_df['item_price'].mean()


"""
7., Készíts egy függvényt, ami visszadja azokat az egyedi termékeket (név, feltét és ár szempontjából egyedi), amelyek ára 10 dollár felett van

függvény név: unique_items_over_ten_dollars
bement: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


def unique_items_over_ten_dollars(input_df):
    new_df = input_df.copy()
    new_df = new_df.drop_duplicates(subset=["item_name", "choice_description", "item_price"])[
        (input_df["item_price"] > 10)]
    return new_df[["item_name", "choice_description", "item_price"]]


"""
8., Készíts egy függvényt, ami visszaadja azon termékek neveit, amelyek neve 'S'-el kezdődik.

fv. neve: items_starting_with_s
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


def items_starting_with_s(input_df):
    new_df = input_df[(input_df['item_name'].str.startswith('S'))]
    return new_df['item_name'].drop_duplicates()


"""
9. Készíts egy függvényt, ami visszaadja az első 3 oszlopot. Használd a tisztított.

fv. név: first_three_columns
bemenet: input_df
return típus: pandas.core.frame.DataFrame
"""


def first_three_columns(input_df):
    return input_df.iloc[:, :3]


"""
10. Készíts egy függvényt, ami visszaadja az összes oszlopot az utolsó 2-on kívül. Használd a tisztított adatokat.

fv. név: every_column_except_last_two
bemenet: input_df
return típus: pandas.core.frame.DataFrame
"""


def every_column_except_last_two(input_df):
    return input_df.iloc[:, :-2]


"""
11. Készíts egy függvényt, amely tetszőleges oszlopokat és sorokat ad vissza a bemeneti adatokból. A sorokat és oszlopokat listák formájában adjuk be a függvénynek. A sorokat egy bemeneti oszlop alapján szűrjük.

fv. név: sliced_view
bemenet: input_df, columns_to_keep, column_to_filter, rows_to_keep
return type: pandas.core.frame.DataFrame

"""


def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    new_df = input_df[input_df[column_to_filter].isin(rows_to_keep)]
    new_df = new_df[columns_to_keep]
    return new_df


"""
12. Készíts egy függvényt, ami a bemeneti adatokat kiegészíti egy 'Quartile' oszloppal. Használd a tisztított adatokat. A kvartilis oszlop értékeit az ár alapján határozza meg:

30 - : 'premium'
20 - 29.99: 'high-cost'
10 - 19.99: 'medium-cost
0 - 9.99: 'low-cost'

fv. név: generate_quartile
bemenet: input_df
return type: pandas.core.frame.DataFrame
"""


def generate_quartile(input_df):
    new_df = input_df.copy()

    def conditions(s):
        if s <= 9.99:
            return 'low-cost'
        elif s <= 19.99:
            return 'medium-cost'
        elif s <= 29.99:
            return 'high-cost'
        else:
            return 'premium'

    new_df['Quartile'] = new_df.item_price.apply(conditions)
    return new_df


"""
13., Készíts egy függvényt, ami minden kvartilis értékhez kiszámítja, az átlagos árat. Használd az előző feladat eredményét bemenetként.

fn név: average_price_in_quartiles
bemenet: input_df
return type: pandas.core.frame.DataFrame
"""


def average_price_in_quartiles(input_df):
    new_df = generate_quartile(input_df)
    new_df = new_df.groupby('Quartile')['item_price'].mean()
    return new_df


"""
14., Készíts egy függvényt ami minden kvartilis esetén visszadja az árak minimális és maximális értékét, valamint az átlagát.

fv. név: minmaxmean_price_in_quartile
bemenet: input_df
return type: pandas.core.frame.DataFrame
"""


def minmaxmean_price_in_quartile(input_df):
    new_df = generate_quartile(input_df)
    new_df2 = new_df.groupby('Quartile')['item_price'].min().to_frame()
    new_df2['max'] = new_df.groupby('Quartile')['item_price'].max()
    new_df2['mean'] = new_df.groupby('Quartile')['item_price'].mean()
    new_df2 = new_df2.rename(columns={"item_price": "min"})
    return new_df2


"""
15. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott distribution osztály felhasználásával (UniformDistribution 0,1 paraméterekkel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List    
függvény neve: gen_uniform_mean_trajectories
"""
from src.utils import distributions as dist
from src.weekly import weekly_test_1 as w1
from src.weekly import weekly_test_2 as w2


def gen_uniform_mean_trajectories(distribution: dist.UniformDistribution, number_of_trajectories, length_of_trajectory):
    l = []
    distribution.rand.seed(42)
    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l


"""
16. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott distribution osztály felhasználásával (LogisticDistribution 1, 3.3 paraméterekkel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List    
függvény neve: gen_logistic_mean_trajectories
"""


def gen_logistic_mean_trajectories(distribution: dist.LogisticDistribution, number_of_trajectories,
                                   length_of_trajectory):
    l = []
    distribution.rand.seed(42)
    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l


"""
17. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott distribution osztály felhasználásával (LaplaceDistribution 1, 3.3 paraméterekkel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List    
függvény neve: gen_laplace_mean_trajectories
"""


def gen_laplace_mean_trajectories(distribution: w2.LaplaceDistribution, number_of_trajectories, length_of_trajectory):
    l = []
    distribution.rand.seed(42)
    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l


"""
18. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott distribution osztály felhasználásával (CauchyDistribution 2,4 paraméterekkel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List    
függvény neve: gen_cauchy_mean_trajectories
"""


def gen_cauchy_mean_trajectories(distribution: dist.CauchyDistribution, number_of_trajectories, length_of_trajectory):
    l = []
    distribution.rand.seed(42)
    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l


"""
19. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott distribution osztály felhasználásával (ChiSquaredDistribution 3 paraméterrel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List    
függvény neve: gen_chi2_mean_trajectories
"""


def gen_chi2_mean_trajectories(distribution: dist.ChiSquaredDistribution, number_of_trajectories, length_of_trajectory):
    l = []
    distribution.rand.seed(42)
    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l
