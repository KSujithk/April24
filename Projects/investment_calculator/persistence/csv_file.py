"""This module provides functionality to store 
the results in a csv file

Author: shaikkhajaibrahim
Created Date: 24/Apr/2024
"""
import csv
RESULTS_FILE_PATH = "results.csv"


def write_result(principal, interest_rate, time, future_value):
    """
    This function writes the result to a csv file
    """
    with open(RESULTS_FILE_PATH, 'a',newline='',encoding='utf-8') as file:
        results_writer = csv.writer(file)
        results_writer.writerow([principal,interest_rate,time,future_value])

def read_all_results():
    """
    This function gives an entire file content with results
    """
    with open(RESULTS_FILE_PATH, 'r', encoding='utf-8') as reader:
        result_reader = csv.reader(reader,delimiter=',')
        for record in result_reader:
            yield record
