def free_cash_flow(operating_cash_flow : float, capital_expenditures : float) -> float :
    return operating_cash_flow - capital_expenditures

def intrinsic_value(growth_rate : float, discount_rate : float = 0.10) -> float :
    return growth_rate - discount_rate