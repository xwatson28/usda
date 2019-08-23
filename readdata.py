#!/usr/bin/env python
from glob import glob
import pandas as pd

def read_pork_file(fname):
    import re
    fhand = open(fname)
    line_number = 0
    results = []
    for line in fhand:
        line = line.rstrip()
        if line_number == 1:
            bits = line.split()
            y = bits[4:7]
            y = (" ").join(y)

            results.append(str(y))
        elif line.startswith('FOR WEEK ENDING: '):

            results.append(str(line[17:]))
        elif line.startswith('Total Load Count'):
            x = re.findall('[0-9]+', line)
            x = '.'.join(x)

            results.append(str(x))
            pass
        line_number += 1
    return {'Report Date' : pd.to_datetime(results[0]).date(),
            'Report For Date' : pd.to_datetime(results[1]).date(),
            'Total Loads' : float(results[2])}

def main():
    # Read pork_exports_historic into a dataframe
    brics = pd.read_csv('pork_output/pork_exports_historic.csv')
    files = glob('pork_output/*.txt')

    # For each text file, get the data and add a new row to the dataframe
    new_records = []
    for file in files:
        results = read_pork_file(file)
        new_records.append(results)
    df_new = pd.DataFrame(new_records)
    df_new = pd.concat((df_new, brics))

    #  write the dataframe to pork_exports_current.csv
    df_new.to_csv('pork_output/pork_exports_current.csv')


if __name__ == '__main__':
    main()
