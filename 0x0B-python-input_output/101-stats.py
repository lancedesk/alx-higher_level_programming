#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
"""


def print_stats(size, status_codes):
    """
    Print the computed statistics.

    Args:
        size (int): Total file size.
        status_codes (dict): Dictionary containing status codes & their counts.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):  # Print status codes in ascending order
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])  # Add file size to the total
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)  # Print final statistics

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
