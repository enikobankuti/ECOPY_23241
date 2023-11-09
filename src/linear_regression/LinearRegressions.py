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
        self.left_hand_side = left_hand_side
        self.right_hand_side = np.column_stack((np.ones(len(right_hand_side)), right_hand_side))
        self.beta = None

    def fit(self):
        X = self.right_hand_side
        y = self.left_hand_side
        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y

    def _calculate_standard_errors(self, X, y, beta, residuals, n, k):
        residual_variance = (residuals @ residuals) / (n - k)
        standard_errors = np.sqrt(np.diagonal(residual_variance * np.linalg.inv(X.T @ X)))
        return standard_errors

    def _calculate_residuals(self, X, y, beta):
        return y - X @ beta

    def get_params(self):
        return pd.Series(self.beta, name='Beta coefficients')

    def get_pvalues(self):
        n, k = self.right_hand_side.shape
        residuals = self._calculate_residuals(self.right_hand_side, self.left_hand_side, self.beta)
        standard_errors = self._calculate_standard_errors(self.right_hand_side, self.left_hand_side, self.beta, residuals, n, k)
        t_statistics = self.beta / standard_errors

        p_values = [2 * (1 - stats.t.cdf(abs(t_stat), n - k)) for t_stat in t_statistics]
        p_values = pd.Series(p_values, name="P-values for the corresponding coefficients")
        return p_values

    def get_wald_test_result(self, R):
        r_matrix = np.array(R)
        r = r_matrix @ self.beta
        n = len(self.left_hand_side)
        m, k = r_matrix.shape
        residuals = self._calculate_residuals(self.right_hand_side, self.left_hand_side, self.beta)
        sigma_squared = np.sum(residuals ** 2) / (n - k)
        h = r_matrix @ np.linalg.inv(self.right_hand_side.T @ self.right_hand_side) @ r_matrix.T
        wald = (r.T @ np.linalg.inv(h) @ r) / (m * sigma_squared)
        p_value = 1 - stats.f.cdf(wald, dfn=m, dfd=n - k)
        return f'Wald: {wald:.3f}, p-value: {p_value:.3f}'

    def get_model_goodness_values(self):
        n, k = self.right_hand_side.shape
        y_pred = self.right_hand_side @ self.beta
        ssr = np.sum((y_pred - np.mean(self.left_hand_side)) ** 2)
        sst = np.sum((self.left_hand_side - np.mean(self.left_hand_side)) ** 2)
        c_r_squared = ssr / sst
        adj_r_squared = 1 - (1 - ssr / sst) * (n - 1) / (n - k)
        result = f"Centered R-squared: {c_r_squared:.3f}, Adjusted R-squared: {adj_r_squared:.3f}"
        return result