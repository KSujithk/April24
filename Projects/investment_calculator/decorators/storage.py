"""This module has code for decorators
"""
from persistence.csv_file import write_result
from persistence.json_file import write_result as json_write

def store_in_csv(func):
    """
    This decorater writes the results to csv file
    """
    def store_results(*args, **kwargs):
        write_result(*args, **kwargs)
        func(*args, **kwargs)
    return store_results


def store_in_json(func):
    """
    This decorater writes the results to csv file
    """
    def store_results(*args, **kwargs):
        json_write(*args, **kwargs)
        func(*args, **kwargs)
    return store_results
