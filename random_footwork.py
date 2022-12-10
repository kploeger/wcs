#! /usr/bin/python3
"""
    mail@kaiploeger.net
"""

import numpy as np
import itertools
import argparse

beats = ['__', '_x', 'x_', '_o', 'o_', 'xx', 'xo', 'ox', 'oo']
rhythm_units = [f'{a}|{b}' for a, b in itertools.product(beats, beats)]

basics = {'sugar push': 3,
          'left side pass': 3,
          'under arm pass': 3,
          'whip': 4,
          'sugar tuck': 3,
          'tuck turn': 3}

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--num_patterns', type=int, default=2)


def build_random_sequence(num_units):
        return np.random.choice(rhythm_units, num_units)


if __name__ == '__main__':

    args = parser.parse_args()

    for count in range(args.num_patterns):
        pattern = np.random.choice(list(basics.keys()))

        print(f'\n{count+1}. {pattern}:')

        sequence = build_random_sequence(basics[pattern])

        for unit in sequence:
            print(unit)




