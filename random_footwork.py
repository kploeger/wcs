#! /usr/bin/python3
"""
    mail@kaiploeger.net
"""

import numpy as np
import itertools
import argparse
import time

from datetime import date


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_patterns', type=int, default=2)
parser.add_argument('-r', '--random', action='store_true')


beats = ['__', '_x', 'x_', '_o', 'o_', 'xx', 'xo', 'ox', 'oo']
rhythm_units = [f'{a}|{b}' for a, b in itertools.product(beats, beats)
                if f'{a}{b}'.count('o') > 0
                if f'{a}{b}'.count('x') < 3]

basics = {'sugar push': 3,
          'left side pass': 3,
          'under arm pass': 3,
          'whip': 4,
          'sugar tuck': 3,
          'tuck turn': 3}


def validate_candidate_unit(unit: str, sequence: list[str]):
    b = sequence[-1][-2:]   # last beat of the sequence
    a = unit[:2]            # first beat of the candidate
    if f'{a}{b}'.count('x') > 2: # not to many x in a row
        return False
    if f'{a}{b}'.count('o') < 1: # at least one weight transfer
        return False
    return True

def build_random_sequence(num_units):
        sequence = [np.random.choice(rhythm_units)]
        while len(sequence) < num_units:
            candidate = np.random.choice(rhythm_units)
            if validate_candidate_unit(candidate, sequence):
                sequence.append(candidate)
        return sequence

def print_sequence(sequence, patterns):
    for count, pattern in enumerate(patterns):
        pattern_units, sequence = sequence[:basics[pattern]], sequence[basics[pattern]:]

        print(f'\n{count+1}. {pattern}:')
        for unit in pattern_units:
            print(unit)


if __name__ == '__main__':

    args = parser.parse_args()

    if not args.random:
        np.random.seed(int(str(date.today()).replace('-','')))

    patterns = [np.random.choice(list(basics.keys())) for _ in range(args.num_patterns)]
    num_rhythm_units = sum(basics[pattern] for pattern in patterns)
    sequence = build_random_sequence(num_rhythm_units)

    print_sequence(sequence, patterns)

