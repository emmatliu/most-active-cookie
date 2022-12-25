#!/usr/bin/env python3

import sys
import argparse

# Function to parse csv in format required for parseCookies

def parseCsv(filename, date):
    countDict = {}

    with open(filename) as file:
        for line in file:
            pair = line.split(',')

            cookie = pair[0]
            ts = pair[1][:pair[1].find('T')] if pair[1].find('T') != -1 else ""

            if not ts or ts != date:
                continue

            if cookie in countDict:
                countDict[cookie] += 1
            else:
                countDict[cookie] = 1

    return [cookie for cookie, count in countDict.items() if count == max(countDict.values())]

# Function to get command line arguments

def parseArgs(inputArgs):
    argParser = argparse.ArgumentParser()

    argParser.add_argument("file") # file
    argParser.add_argument("-d") # date

    args = argParser.parse_args(inputArgs)

    return args.file, args.d

# Main function

def main():
    filename, date = parseArgs(sys.argv[1:])
    res = parseCsv(filename, date)
    print('\n'.join(res))

if __name__ == "__main__":
    main()