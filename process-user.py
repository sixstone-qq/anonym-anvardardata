#!/usr/bin/env python3

"""Program to gather as tuple form isolated user data"""
import argparse
import json
import os
import os.path


from util.sumdiv import sum_div


# Constants
AIRLINE_TICKET = 'airline'


def process_file(filename, purchase_type):
    """Open a JSON file and read the purchases. It returns a single
    dictionary with type of purchase as key and the total amount as
    value.

    Example: {'pillow': 25, 'airline': 50000}
    """
    with open(filename) as f:
        try:
            file_content = json.load(f)
        except ValueError:
            return None, None  # Impossible to parse

    user_id, _ = os.path.splitext(os.path.basename(filename))

    user_result = {}
    if 'purchases' in file_content:
        for row in file_content['purchases']:
            if row['type'] == purchase_type:
                user_result.setdefault(row['amount'], 0)
                user_result[row['amount']] += 1

    # Divide the sum of amount of ticket purchase to maximise the
    # matching ocurrences with other pydusers
    final_result = []
    for amount, total in user_result.items():
        final_result = [(amount, x) for x in sum_div(total)]

    return user_id, final_result


def print_header():
    print("| first | second |")
    print("|-------|--------|")


def report(result_set):
    for t in result_set[1]:
        print("| {0:5} | {1:6} |".format(*t))


def arg_parser():
    parser = argparse.ArgumentParser(
        description="""Parse a folder with users' purchases
                       in JSON-formatted files"""
    )
    parser.add_argument('--type', type=str, metavar="PURCHASE_TYPE",
                        help="Type of purchase to extract data from",
                        default=AIRLINE_TICKET)
    parser.add_argument('folder', type=str,
                        help="Directory where JSON user's files are")
    return parser


def main():
    parsed_args = arg_parser().parse_args()
    header_printed = False
    for root, dirs, files in os.walk(parsed_args.folder):
        for file_name in files:
            rs = process_file(os.path.join(root, file_name),
                              parsed_args.type)
            if rs[0] is None and rs[1] is None:
                continue  # Error processing that file
            if rs[0] and not header_printed:
                print_header()
                header_printed = True
            report(rs)

        # FIXME: Do it recursively


if __name__ == '__main__':
    main()
