"""This module will have functions to calculate
lumpsum returns

Author: shaikkhajaibrahim
Date: 21/Apr/2024
"""

def returns(
        prinicpal,
        intrest_rate,
        time_in_years,
        n=1):
    """This function calculates lumpsum returns

    Arguments:
      principal: Present value of investment
      intrest_rate: Rate of return
      time_in_years: Duration of investment
      n: Number of compounded interests in a year
    """
    result = prinicpal * (1 + ((intrest_rate/100)/n)) ** (n * time_in_years)
    return round(result,2)
