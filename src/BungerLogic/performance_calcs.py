from typing import Sequence, overload
from formulas import compound_annual_growth_rate

@overload
def consistent_earnings_growth(earnings : Sequence[float]) -> float :
    return compound_annual_growth_rate(earnings)

def consistent_earnings_growth(first_earning : float, last_earning : float, years_elapsed : float) -> float :
    return compound_annual_growth_rate(first_earning, last_earning, years_elapsed)

def owner_earnings(net_income : float, depreciation_amortization : float, capital_expenditures : float) -> float :
    return net_income - depreciation_amortization - capital_expenditures

def earnings_yield(eps : float, share_price : float) -> float :
    return eps / share_price

def return_on_invested_capital(nopat : float, debt : float, equity : float, cash : float) -> float :
    return nopat / (debt + equity - cash)