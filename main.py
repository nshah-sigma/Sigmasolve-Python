'''
You are the owner of a grocery store and would like to build an application for your employees to easily find items. 
Your task is to create an application that accepts user input and allows them to filter data from an existing CSV file.
input file: products.csv

testing input

> 2.40 2.60 JAN-01-2019 JAN-31-2019

testing output

> 2.40 2.60 JAN-01-2019 JAN-31-2019
+------+-------------------------------+---------+------------+
|   id | name                          |   price | expires    |
|------+-------------------------------+---------+------------|
|  505 | Limes                         |    2.47 | 01/22/2019 |
|  553 | Soup - Campbells - Tomato     |    2.49 | 01/08/2019 |
|  661 | Wine - Rosso Del Veronese Igt |    2.5  | 01/17/2019 |
|  923 | Bacardi Mojito                |    2.52 | 01/14/2019 |
+------+-------------------------------+---------+------------+

'''

from datetime import datetime
import pandas as pd
from tabulate import tabulate



def display_table(sp):
    """
    Display product table
    """
    PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP = sp
    if '*' in PRICE_MIN:
        PRICE_MIN = 0
    if '*' in PRICE_MAX:
        PRICE_MAX = 999999
    if '*' in EXPIRES_START:
        EXPIRES_START = 'JAN-01-1970'
    if '*' in EXPIRES_STOP:
        EXPIRES_STOP = 'DEC-31-3000'
        
    csv_reader = pd.read_csv('products.csv')

    start = datetime.strptime(EXPIRES_START, '%b-%d-%Y').strftime('%m/%d/%Y')

    stop = datetime.strptime(EXPIRES_STOP, '%b-%d-%Y').strftime('%m/%d/%Y')

    df = csv_reader.loc[(csv_reader['price'] >= float(PRICE_MIN)) & (csv_reader['price'] <= float(PRICE_MAX)) & (csv_reader['expires'] >= start) & (csv_reader['expires'] <= stop)]
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))


def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        if value == 'exit':
            break
        else:
            values = value.split(' ')
            if len(values) != 4:  # checking if enough data points are given
                print('Supply only 4 values or type exit')
            else:
                PRICE_MIN = values[0]
                PRICE_MAX = values[1]
                EXPIRES_START = values[2]
                EXPIRES_STOP = values[3]
                search_params = (PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP)
                display_table(search_params)


if __name__ == '__main__':
    start()