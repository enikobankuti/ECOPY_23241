import numpy as np
import statsmodels.api as sm
import pandas as pd
import scipy.stats as stats
from scipy.stats import t, norm
from scipy.optimize import minimize


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
        standard_errors = self._calculate_standard_errors(self.right_hand_side, self.left_hand_side, self.beta,
                                                          residuals, n, k)
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


class LinearRegressionGLS:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.n = right_hand_side.shape[0]
        self.X = np.concatenate((np.ones((self.n, 1)), right_hand_side), axis=1)
        self.k = self.X.shape[1]
        self.dof = self.n - self.k

    def fit(self):
        ols_betas = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.left_hand_side
        ols_resid = self.left_hand_side - self.X @ ols_betas
        y = np.log(ols_resid ** 2)
        log_betas = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ y
        predictions = np.sqrt(np.exp(self.X @ log_betas))
        self.v_inv = np.diag(1.0 / predictions)
        self.gls_betas = np.linalg.inv(self.X.T @ self.v_inv @ self.X) @ self.X.T @ self.v_inv @ self.left_hand_side

    def get_params(self):
        names = ["Intercept"] + [f"X{i}" for i in range(1, self.k)]
        values = [self.gls_betas[0]] + list(self.gls_betas[1:])
        return pd.Series(values, index=names, name="Coefficients")

    def get_pvalues(self):
        self.gls_residuals = self.left_hand_side - self.X @ self.gls_betas
        self.gls_variance = self.gls_residuals.T @ self.gls_residuals / self.dof
        self.gls_SE = np.sqrt(np.diag(self.gls_variance * np.linalg.inv(self.X.T @ self.v_inv @ self.X)))
        t_values = self.gls_betas / self.gls_SE
        p_values = 2 * (1 - stats.t.cdf(np.abs(t_values), self.dof))
        return pd.Series(p_values, name="P-values for the corresponding coefficients")

    def get_wald_test_result(self, constraints):
        R = np.asmatrix(constraints)
        m = R.shape[0]
        RBr = R @ self.gls_betas
        RXTXRT = R @ np.linalg.inv(self.X.T @ self.v_inv @ self.X) @ R.T
        wald_value = RBr @ np.linalg.inv(RXTXRT) @ RBr.T / m / self.gls_variance
        p_value = 1 - stats.f.cdf(wald_value.item(), m, self.dof)
        return f"Wald: {wald_value.item():.3f}, p-value: {p_value:.3f}"

    def get_model_goodness_values(self):
        SST = self.left_hand_side.T @ self.v_inv @ self.left_hand_side
        SSR = self.left_hand_side.T @ self.v_inv @ self.X @ np.linalg.inv(
            self.X.T @ self.v_inv @ self.X) @ self.X.T @ self.v_inv @ self.left_hand_side
        crs = 1 - SSR / SST
        ars = 1 - (1 - crs) * (self.n - 1) / self.dof
        return f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"




class LinearRegressionML:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

    def calculate_res(self, X, y, coefficients):
        return y - np.dot(X, coefficients)

    def calculate_p_values(self, coefficients, X, y):
        n, k = X.shape
        res = self.calculate_res(X, y, coefficients)
        sigma_squared = np.sum(res ** 2) / (n - k)
        var_beta = np.linalg.inv(X.T @ X) * sigma_squared
        t_statistic = coefficients / np.sqrt(np.diag(var_beta))
        p_values = 2 * (1 - t.cdf(np.abs(t_statistic), df=n-k))
        return p_values

    def neg_loglikelihood(self, params):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        b0, b1, b2, b3, sigma_sq = params
        betas = np.array([b0, b1, b2, b3])
        p = X @ betas
        likeli = np.sum(stats.norm.logpdf(y, p, sigma_sq))

        return -likeli

    def fit(self):
        opt = minimize(self.neg_loglikelihood, np.array([.1, .1, .1, .1, .1]), method='L-BFGS-B')
        b0, b1, b2, b3, sigma_sq = opt.x

        self.coefficients = np.array([b0, b1, b2, b3])
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        n, k = X.shape
        self.res = y - X @ self.coefficients
        sigma_sq = np.sum(self.res ** 2) / (n - k)
        var_b = np.linalg.inv(X.T @ X) * sigma_sq
        t_stat = self.coefficients / np.sqrt(np.diag(var_b))
        self.p_values = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=n-k))
        rss = np.sum(self.res ** 2)
        tss = np.sum((y - np.mean(y)) ** 2)
        self.crs = 1 - rss / tss
        self.ars = 1 - (rss / (n - k)) / (tss / (n - 1))

    def get_params(self):
        return pd.Series(self.coefficients, name='Beta coefficients')

    def get_pvalues(self):
        index = ['Intercept'] + list(self.right_hand_side.columns)
        return pd.Series(self.p_values, index=index, name='P-values for the corresponding coefficients')

    def get_model_goodness_values(self):
        return f'Centered R-squared: {self.crs:.3f}, Adjusted R-squared: {self.ars:.3f}'
