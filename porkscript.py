#!/usr/bin/env python


import urllib.request, urllib.parse, urllib.error
from datetime import date, datetime, timedelta
import os.path

PORK_URL = 'https://www.ams.usda.gov/mnreports/lm_pk640.txt'
OUTPUT_DIR = 'pork_output/'

def find_most_recent_file(today):
    """
    Looks back 10 days to see if any file has been saved in
    OUTPUT_DIR and returns the name of that file.  Otherwise returns
    None.
    """
    most_recent = None

    for i in range(10):

        # get the date i days ago
        date_n_days_ago = datetime.now() - timedelta(i)
        print(date_n_days_ago.date())

        fn = OUTPUT_DIR + str(date_n_days_ago.date()) + '.txt'
        if os.path.exists(fn) == True:
            most_recent = fn
            break

    return most_recent

def get_data_from_url():

    data = ""
    fhand = urllib.request.urlopen(PORK_URL)
    for line in fhand:
        data += str(line.decode().rstrip()) + '\n'
        pass
    fhand.close()
    return data

def read_file(filename):
    data = ""
    fhand = open(filename)
    for line in fhand:
        data += str(line)
        pass
    fhand.close()
    return data

def write_data_to_file(filename, data):
    fho = open(filename, 'w')
    fho.write(data)
    fho.close()
    return

def check_changed(data1, data2):
    if data1 != data2:
        print('Data has changed')
    else:
        print('Nothing to do')
    return data1 != data2


def main():
    today = date.today()

    # Find the last file you saved
    most_recent = find_most_recent_file(today)
    data = get_data_from_url()
    most_recent_data = read_file(most_recent)
    if check_changed(data, most_recent_data):
        newtextfile = OUTPUT_DIR + str(today) + '.txt'
        write_data_to_file(newtextfile, data)
        pass

    return()


if __name__ == '__main__':
    main()
