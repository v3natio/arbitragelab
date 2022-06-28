"""
This module implements Cointegration-based Statistical Arbitrage strategies.
"""
from arbitragelab.cointegration_approach.johansen import JohansenPortfolio
from arbitragelab.cointegration_approach.engle_granger import EngleGrangerPortfolio
from arbitragelab.cointegration_approach.minimum_profit import MinimumProfit
from arbitragelab.cointegration_approach.coint_sim import CointegrationSimulation
from arbitragelab.cointegration_approach.multi_coint import MultivariateCointegration
from arbitragelab.cointegration_approach.sparse_mr_portfolio import SparseMeanReversionPortfolio
from arbitragelab.cointegration_approach.utils import (get_half_life_of_mean_reversion, get_hurst_exponent)
