#!/usr/bin/env python

from gendiff.cli import parse
from gendiff.gen_diff import generate_diff


def main():
    args = parse()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
