"""
Az órán elhangzott, hogy ne a weekly_test_6 fájlba mentsük a megoldásokat, ezért raktam a df-es részt is ide..
de akkor most létrehoztam a weekly_test_6-ot, bízom benne, hogy így megfelelő. A notebookban is benne vannak egyébként a megoldásaim.
Mellesleg nálam lefuttottak a tesztek eddig is minden gond nélkül.

numpy-t kivettem
"""

import statsmodels.api as sm
import pandas as pd

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

        fvalue = round(float(wald_test_result.statistic[0, 0]), 2)
        pvalue = round(float(wald_test_result.pvalue), 3)

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
