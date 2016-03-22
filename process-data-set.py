#!/usr/bin/env python3

"""Program to agreggrate and anonymisation of a data set from users"""
import argparse
import re
import sys


from itertools import chain, groupby
from statistics import mean, median
from util.constant import COL_HEADER, ROW_SEP


# Constants
MIN_ANON_THRESHOLD = 5


def parse_input(in_f):
    """Parse a valid input file. Raise ValueError in any parsing error"""
    # Read two first lines of headers
    for expected in (COL_HEADER, ROW_SEP):
        line = in_f.readline().strip()
        if line != expected:
            raise ValueError("'{}' is expected. Found: '{}'".format(
                expected, line))

    # Read rows
    tuple_list = []
    for line in in_f:
        parsed_exp = re.match('\|\s+(\d+)\s+\|\s+(\d+)\s+\|', line)
        if parsed_exp is None:
            raise ValueError(
                "Invalid line: {} Expected: | num | num |".format(line)
            )
        tuple_list.append([int(g) for g in parsed_exp.groups()])

    return tuple_list


def anonymise(l):
    # Aggregate given tuples to triplets
    sorted_l = sorted(l)
    aggr = [k + [len(list(g))] for k, g in groupby(sorted_l)]
    # Anonymise the result by discarding triplets with
    # MIN_ANON_THRESHOLD or less
    anon_aggr = [t for t in aggr if t[2] >= MIN_ANON_THRESHOLD]
    return anon_aggr


def derive(l):
    min_val = min([t[0] for t in l])
    max_val = max([t[0] for t in l])
    expanded_list = list(chain.from_iterable(
        [[t[0] for i in range(t[1])] for t in l]
    ))
    avg_val = mean(expanded_list)
    median_val = median(expanded_list)
    return min_val, max_val, avg_val, median_val


def arg_parser():
    parser = argparse.ArgumentParser(
        description="""Given a user's dataset, perform an aggregation
                       and anonymisation process to derive the minimum,
                       maximum, average and median values"""
    )
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    return parser


def main():
    parsed_args = arg_parser().parse_args()
    parsed_data = parse_input(parsed_args.infile)
    # Anonymise
    anon_data = anonymise(parsed_data)
    min_data, max_data, avg_data, median_data = derive(anon_data)
    print("""
- min: {}\n
- max: {}\n
- average: {}\n
- median: {}""".format(min_data, max_data, avg_data, median_data))


if __name__ == '__main__':
    main()
