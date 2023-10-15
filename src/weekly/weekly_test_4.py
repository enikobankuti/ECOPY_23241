# %% md
## Az eredményeket mentsd a src/weekly modul-ba weekly_test_4.py néven
# %% md
#### Használható modulok: pandas, typing, matplotlib, random, src.distributions, src.weekly
# %%
import pandas
import pandas as pd
from typing import List, Dict
import matplotlib
import matplotlib.pyplot as plt

# %%
"""
1., Olvasd be a data mappa Euro_2012_stats_TEAM.csv nevű fájlját egy dataframe-be. A betöltött adatokat az euro12 alatt tárolja. A következő feladatokban a kiinduló fájlt ne írd felül.
"""
# %%
df_data = pd.read_csv('/Users/Enci/Documents/GitHub/ECOPY_23241/data/Euro_2012_stats_TEAM.csv')
# %%

# %%
"""
2., Készíts egy függvényt, ami megmondja, hogy hány csapat indult az Európa Bajnokságon

függvény név: number_of_participants
bemenet: input_df
kimeneti típus: int
"""


# %%
def number_of_participants(input_df):
    return len(input_df['Team'])


# %%

# %%
"""
3., Készíts egy függvényt, ami visszadja a csapatokat és az áltatuk lőtt gólokat.

függvény név: goals
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


# %%
def goals(input_df):
    new_df = input_df.copy()
    new_df = new_df[['Team', 'Goals']]

    return new_df


# %%

# %%
"""
4., Készíts egy függvényt, ami sorba rendezi az országokat a lőtt gólok száma alapján csökkenő sorrendben. Használd az előző  függvény eredményét.

függvény név: sorted_by_goal
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame

"""


# %%
def sorted_by_goal(input_df):
    new_df = goals(input_df)
    return new_df.sort_values(by=['Goals'], ascending=False)


# %%

# %%
"""
5., Készíts egy függvényt, ami visszaadja az átlagos gól számot.

függvény név: avg_goal
bemenet: input_df
kimeneti típus: float

"""


# %%
def avg_goal(input_df):
    return input_df['Goals'].mean()


# %%

# %%
"""
6., Készíts egy függvényt, ami visszadja azokat az országokat akik 6 vagy több gólt rúgtak

függvény név: countries_over_five
bement: input_df
kimeneti típus: pandas.core.frame.DataFrame

"""


# %%
def countries_over_five(input_df):
    new_df = input_df.copy()
    new_df = input_df[(input_df['Goals'] > 5)]
    return new_df[['Team']]


# %%

# %%
"""
7., Készíts egy függvényt, ami visszaadja azon országok neveit, amelyek neve 'G'-vel kezdődik

fv. neve: countries_starting_with_g
bemenet: input_df
kimeneti típus: pandas.core.frame.DataFrame
"""


# %%
def countries_starting_with_g(input_df):
    new_df = input_df.copy()
    new_df = input_df[(input_df['Team'].str.startswith('G'))]
    return new_df['Team']


# %%

# %%
"""
8. Készíts egy függvényt, ami visszaadja az első 7 oszlopot. Használja a kiinduló adatokat

fv. név: first_seven_columns
bemenet: input_df
return típus: pandas.core.frame.DataFrame

"""


# %%
def first_seven_columns(input_df):
    return input_df.iloc[:, :7]


# %%

# %%
"""
9. Készíts egy függvényt, ami visszaadja az összes oszlopot az utolsó 3-on kívül. Használja a kiinduló adatokat

fv. név: every_column_except_last_three
bemenet: input_df
return típus: pandas.core.frame.DataFrame

"""


# %%
def every_column_except_last_three(input_df):
    return input_df.iloc[:, :-3]


# %%

# %%
"""
10. Készíts egy függvényt, amely tetszőleges oszlopokat és sorokat ad vissza a bemeneti adatokból. A sorokat és oszlopokat listák formájában adjuk be a függvénynek. A sorokat egy bemeneti oszlop alapján szűrjük

fv. név: sliced_view
bemenet: input_df, columns_to_keep, column_to_filter, rows_to_keep
return type: pandas.core.frame.DataFrame

"""


# %%
def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    new_df = input_df[columns_to_keep]
    new_df = new_df[new_df[column_to_filter].isin(rows_to_keep)]

    return new_df


"""
11. Készíts egy függvényt, ami a bemeneti adatokat kiegészíti egy 'Quartile' oszloppal. A kvartilis oszlop értékeit a lőtt gólok alapján határozza meg:

6 - 12: 1
5 - 5: 2
3 - 4: 3
0 - 2: 4

fv. név: generate_quartile
bemenet: input_df
return type: pandas.core.frame.DataFrame

"""


# %%
def generate_quarters(input_df):
    new_df = input_df.copy()

    def conditions(s):
        if s <= 2:
            return 4
        elif s <= 4:
            return 3
        elif s <= 5:
            return 2
        else:
            return 1

    new_df['Quartile'] = new_df.Goals.apply(conditions)
    return new_df


# %%
# %%
"""
12., Készíts egy függvényt, ami minden kvartilis értékhez kiszámítja, hogy átlagosan hány passzot adtak.

fn név: average_yellow_in_quartiles
bemenet: input_df
return type: pandas.core.frame.DataFrame

"""


# %%
def average_yellow_in_quartiles(input_df):
    new_df = generate_quarters(input_df)
    new_df = new_df.groupby('Quartile')['Passes'].mean().reset_index(drop=True)
    return new_df


# %%

# %%
"""
13., Készíts egy függvényt ami minden kvartilis esetén visszadja a blokkok (Blocks) minimális és maximális értékét.

fv. név: minmax_block_in_quartile
bemenet: input_df
return type: pandas.core.frame.DataFrame
"""


# %%
def minmax_block_in_quartile(input_df):
    new_df = generate_quarters(input_df)
    new_df = new_df.groupby('Quartile')
    return new_df['Blocks'].agg(['min', 'max'])


# %%

# %%
"""
14., Készíts egy függvényt, ami scatter_plot-on ábrázolja a gólok és a kaput ért találatok kapcsolatát.

fv név: scatter_goals_shots
bemenet: input_df
X tengelyen: Goals
y tengelyen: Shots on target
title: 'Goals and Shot on target'
Tengely feliratok egyezenek meg az oszlop nevekkel

return type: matplotlib.figure.Figure
"""


def scatter_goals_shots(input_df):
    fig, ax = plt.subplots()
    ax.scatter(x=input_df['Goals'], y=input_df['Shots on target'])

    ax.set_xlabel('Goals')
    ax.set_ylabel('Shot on target')
    ax.set_title('Goals and Shot on target')

    return fig


"""
15., Készíts egy függvényt, ami scatter_plot-on ábrázolja a gólok és a kaput ért találatok kapcsolatát. A különböző kvartiliseket különböző színek jelöljék. A színek mellett jelenjen meg jelmagyarázat.

fv név: scatter_goals_shots_by_quartile
bemenet: input_df
X tengelyen: Goals
y tengelyen: Shots on target
title: 'Goals and Shot on target'
Tengely feliratok egyezenek meg az oszlop nevekkel
Jelmagyarázat címe: Quartiles

return type: matplotlib.figure.Figure
"""


# %%
def scatter_goals_shots_by_quartile(input_df):
    new_df = generate_quarters(input_df)
    fig, ax = plt.subplots()

    ax.scatter(x=new_df['Goals'], y=new_df['Shots on target'], c=new_df["Quartile"], label=new_df["Quartile"])

    ax.set_xlabel('Goals')
    ax.set_ylabel('Shot on target')
    ax.set_title('Goals and Shot on target')
    return fig


# %%

# %%
"""
16. Készíts egy függvényt, ami létrehoz egy listát, benne number_of_trajectories db listával. A belső listák létrehozásának logikája a következő:
    A bemeneti paraméterként kapott pareto_distribution osztály felhasználásával (ParetoDistribution 1,1 paraméterekkel) generálj length_of_trajectory véletlen számot
    A belső lista tartalmazza a generált számok kumulatív átlagát.
    Ismételd meg number_of_trajectories alkalommal (mindegyik belső listába egyszer)
    A seed értéke legyen 42.

függvény bemenete: pareto_distribution, number_of_trajectories, length_of_trajectory
kimeneti típus: List
függvény neve: gen_pareto_mean_trajectories
"""
# %%
from tests.utils import test_distributions as dist
from src.weekly import weekly_test_1 as w1
from src.weekly import weekly_test_2 as w2


def gen_pareto_mean_trajectories(pareto_distribution: w2.ParetoDistribution, number_of_trajectories,
                                 length_of_trajectory):
    l = []
    pareto_distribution.rand.seed(42)

    for i in range(0, number_of_trajectories):
        rand_num = []
        for j in range(0, length_of_trajectory):
            rand_num.append(pareto_distribution.gen_rand())
        l.append(w1.cumavg_list(rand_num))
    return l



# %%
