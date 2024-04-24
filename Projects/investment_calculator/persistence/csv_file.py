"""This module provides functionality to store 
the results in a csv file

Author: shaikkhajaibrahim
Created Date: 24/Apr/2024
"""
import csv
import os
RESULTS_FILE_PATH = "results.csv"


def write_result(principal, interest_rate, time, investment_type, future_value):
    """
    This function writes the result to a csv file
    """
    file_exists = False
    if os.path.exists(RESULTS_FILE_PATH):
        file_exists = True

    with open(RESULTS_FILE_PATH, 'a',newline='',encoding='utf-8') as file:
        results_writer = csv.writer(file)
        if not file_exists:
            results_writer.writerow(
                [
                    'principal',
                    'interest_rate',
                    'time',
                    'investment_type',
                    'future_value'
                    ]
            )
        results_writer.writerow([principal,interest_rate,time,investment_type,future_value])

def read_all_results():
    """
    This function gives an entire file content with results
    """
    with open(RESULTS_FILE_PATH, 'r', encoding='utf-8') as reader:
        result_reader = csv.reader(reader,delimiter=',')
        for record in result_reader:
            # todo skip first record as it is header
            yield record
