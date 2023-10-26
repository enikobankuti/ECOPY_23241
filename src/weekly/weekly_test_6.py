from pathlib import Path
datalib = Path.cwd().parent.joinpath('data')
import pandas as pd

data = pd.read_parquet('/Users/Enci/Documents/GitHub/ECOPY_23241/data/sp500.parquet', engine='fastparquet')

data2 = pd.read_parquet('/Users/Enci/Documents/GitHub/ECOPY_23241/data/ff_factors.parquet', engine='fastparquet')

merge_data = pd.merge(data, data2, on='Date', how='left')

merge_data['Excess Return'] = merge_data['Monthly Returns'] - merge_data['RF']

merge_data = merge_data.sort_values(by=['Symbol', 'Date'])
merge_data['ex_ret_1'] = merge_data.groupby('Symbol')['Excess Return'].shift(-1)

merge_data = merge_data.dropna(subset=['ex_ret_1'])
merge_data = merge_data.dropna(subset=['HML'])

amazon = merge_data[merge_data['Symbol'] == 'AMZN']
amazon = amazon.drop(columns=['Symbol'])
