# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
#This is a function to save a csvfile

def save_csv(csvpath,qualifying_loans,header):
    with open(csvpath,"w")as csvfile:
        csvwriter=csv.writer(csvfile)
       # csvwriter.writerow(header)
       # for loan in qualifying_loans:
            #csvwriter.writerow(loan.value())
        if header:
            csvwriter.writerow(header)    
        csvwriter.writerows(qualifying_loans)

