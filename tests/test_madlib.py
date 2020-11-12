from madlib_cli.madlib import read_template, parse

import re

open_file = open('assets/game.txt').read()

path = 'assets/game.txt'

string_template = read_template('assets/game.txt')

def test_read_template():
    actual = read_template(path)
    expected = open_file.strip()
    assert actual == expected


def test_parse():
    actual = parse(string_template)
    expected = '''
    Make Me A Video Game!

    I the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!

    What are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.
    '''
    assert actual == expected