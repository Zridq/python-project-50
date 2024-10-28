import argparse
from gendiff.makediff import generate_diff
from gendiff.parse_file import parse_file


def main():
    parser = argparse.ArgumentParser(description="""Compares
     two configuration files and shows a difference.""")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = parse_file(args.first_file)
    second_file = parse_file(args.second_file)
    if args.format is None:
        args.format = 'stylish'
    return print(generate_diff(first_file, second_file, args.format))


if __name__ == "__main__":
    main()
