import argparse
import sys


def sys_arguments():
    # print('sys.argv = ' + repr(sys.argv))
    assert type(sys.argv) == list


def my_sum(args):
    return sum(args)


def parse_arguments():
    # Create parser.
    parser = argparse.ArgumentParser(description='Process arguments.')

    # Add positional argument
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    # Add optional argument
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=my_sum, default=max,
                        help='sum the integers (default: find the max)')

    # Parse arguments
    if len(sys.argv) > 1:
        parser.parse_args()
    else:
        s = ['--sum', '7', '-1', '42']
        p = vars(parser.parse_args(s))
        x = p['accumulate'](p['integers'])
        print(p)
        assert x == 48


if __name__ == "__main__":
    sys_arguments()
    parse_arguments()
