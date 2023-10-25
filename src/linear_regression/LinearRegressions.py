""" first part """

from pathlib import Path

datalib = Path.cwd().parent.joinpath('data')
import pandas as pd
import numpy as np

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

""" second part """
import statsmodels.api as sm


class LinearRegressionSM:

    def __init__(self, left_hand_side, right_hand_side):
        self._model = None
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

    def fit(self):
        right_df = sm.add_constant(self.right_hand_side)
        model = sm.OLS(self.left_hand_side, right_df).fit()
        self._model = model

    def get_params(self):
        beta_coefficients = self._model.params
        beta_series = pd.Series(beta_coefficients, name='Beta coefficients')
        return beta_series

    def get_pvalues(self):
        p_values = self._model.pvalues
        p_values_series = pd.Series(p_values, name='P-values for the corresponding coefficients')
        return p_values_series

    def get_wald_test_result(self, restriction_matrix):
        wald_test_result = self._model.wald_test(restriction_matrix)

        fvalue = np.round(wald_test_result.statistic[0, 0], 2)
        pvalue = np.round(wald_test_result.pvalue, 3)

        result_string = f"F-value: {fvalue}, p-value: {pvalue}"

        return result_string

    def get_model_goodness_values(self):
        r_squared = self._model.rsquared_adj
        aic = self._model.aic
        bic = self._model.bic

        ars = f"{r_squared:.3f}"
        ak = f"{aic:.2e}"
        by = f"{bic:.2e}"

        result_string = f"Adjusted R-squared: {ars}, Akaike IC: {ak}, Bayes IC: {by}"

        return result_string
