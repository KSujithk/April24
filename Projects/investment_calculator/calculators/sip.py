"""This module is used for calculating 
systematic investments

Assumptions:
  This calculator as of now expects the investment is done monthly
Formula
FV= P * (( (1+i) ** (n) - 1)/i) * (1 + i)

    FV= Future value of investment 

    P= investment amount 

    i= SIP return rate per period 

    n= total period of investment 
"""

def returns(
        invested_amount,
        return_rate,
        total_period_years):
    """
    This method calculates returns of monthly sip
    """
    n = total_period_years * 12
    i = (return_rate/12)/100
    future_value = invested_amount * (( (1+i) ** (n) - 1)/i) * (1 + i)
    return future_value
