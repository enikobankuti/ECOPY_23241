import numpy as np
import statsmodels.api as sm
import pandas as pd
import scipy.stats as stats


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


class LinearRegressionNP:
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
        t_values = self._model.tvalues
        p_values = (1 - stats.t.cdf(np.abs(t_values), self._model.df_resid)) * 2
        p_series = pd.Series(p_values, 1 - p_values, name='P-values for the corresponding coefficients')
        return p_series

    def get_wald_test_result(self, R):
        wald_result = self._model.wald_test(R)
        wald_value = float(wald_result.statistic)
        p_value = float(wald_result.pvalue)
        result_string = f"Wald: {wald_value:.3f}, p-value: {p_value:.3f}"
        return result_string

    def get_model_goodness_values(self):
        rsquared = self._model.rsquared
        adj_rsquared = self._model.rsquared_adj
        result_string = f"Centered R-squared: {rsquared:.3f}, Adjusted R-squared: {adj_rsquared:.3f}"
        return result_string
