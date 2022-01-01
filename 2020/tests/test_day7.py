from puzzles.day7 import get_puzzle_input

def test_get_puzzle_input():
    filename = '../data/inputday7_test.txt'
    assert ('muted yellow',2,'shiny gold') in get_puzzle_input(filename)