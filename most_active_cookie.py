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

    return arg_parser.parse_args(input_args)

def get_output(cookies):
    """
    Prints each cookie in cookies on a new line.

    cookies -- list of cookies from parse_csv
    """
    if cookies: # If no cookies, we don't want a newline from the print
        print('\n'.join(cookies))

def main():
    """
    Main function calling get_args and parse_csv to get the max count cookies.
    """
    args = get_args(sys.argv[1:])
    cookies = parse_csv(args.file, args.d)
    get_output(cookies)

if __name__ == "__main__":
    main()
