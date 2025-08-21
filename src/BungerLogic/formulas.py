from typing import Sequence, overload

@overload
def compound_annual_growth_rate(values : Sequence[float]) -> float : 
    if len(values) < 2:
        raise ValueError("Two or more values required to calculate CAGR")
    
    start, end = values[0], values[-1]
    period = len(values) - 1

    return (end / start) ** (1 / period) - 1

def compound_annual_growth_rate(first : float, last : float, separation : float) -> float : 
    return (last / first) ** (1 / separation) - 1