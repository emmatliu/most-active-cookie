#!/usr/bin/env python3

"""
sys - get arguments
argparse - parse arguments
"""
import sys
import argparse

def parse_csv(filename, date):
    """
    Parse the csv file and create a count dictionary of cookies with timestamp on specified day

    filename -- csv file name
    date -- the specified date argument
    """
    count_dict = {}

    with open(filename, encoding='utf-8') as file:
        for line in file:
            pair = line.split(',')

            # get cookie and processed date from timestamp portion
            cookie = pair[0]
            timestamp_date = pair[1][:pair[1].find('T')] if pair[1].find('T') != -1 else ""

            # invalid or not a date we want
            if not timestamp_date or timestamp_date != date:
                continue

            # update count dictionary
            if cookie in count_dict:
                count_dict[cookie] += 1
            else:
                count_dict[cookie] = 1

    # list of most active cookies
    return [cookie for cookie, count in count_dict.items() if count == max(count_dict.values())]

def get_args(input_args):
    """
    Get arguments from the command line.

    input_args -- command line arguments
    """
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("file") # file option
    arg_parser.add_argument("-d") # date option

    args = arg_parser.parse_args(input_args)

    return args.file, args.d

def main():
    """
    Main function calling get_args and parse_csv to get the max count cookies.
    """
    filename, date = get_args(sys.argv[1:])
    res = parse_csv(filename, date)
    print('\n'.join(res)) # prints each cookie on new line

if __name__ == "__main__":
    main()
