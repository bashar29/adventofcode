from puzzles.day5 import (get_row_from_boarding_pass,get_column_from_boarding_pass,
                            compute_seat_id)

def test_get_row_from_boarding_pass():
    boarding_pass = [*'BFFFBBFRRR']
    assert get_row_from_boarding_pass(boarding_pass) == 70
    boarding_pass = [*'FFFBBBFRRR']
    assert get_row_from_boarding_pass(boarding_pass) == 14
    boarding_pass = [*'BBFFBBFRLL']
    assert get_row_from_boarding_pass(boarding_pass) == 102
    boarding_pass = [*'FBFBBFFRLR']
    assert get_row_from_boarding_pass(boarding_pass) == 44

def test_get_column_from_boarding_pass():
    boarding_pass = [*'BFFFBBFRRR']
    assert get_column_from_boarding_pass(boarding_pass) == 7
    boarding_pass = [*'FFFBBBFRRR']
    assert get_column_from_boarding_pass(boarding_pass) == 7
    boarding_pass = [*'BBFFBBFRLL']
    assert get_column_from_boarding_pass(boarding_pass) == 4
    boarding_pass = [*'FBFBBFFRLR']
    assert get_column_from_boarding_pass(boarding_pass) == 5

def test_compute_seat_id():
    boarding_pass = [*'BFFFBBFRRR']
    assert compute_seat_id(70,7) == 567
    boarding_pass = [*'FFFBBBFRRR']
    assert compute_seat_id(14,7) == 119
    boarding_pass = [*'BBFFBBFRLL']
    assert compute_seat_id(102,4) == 820
    boarding_pass = [*'FBFBBFFRLR']
    assert compute_seat_id(44,5) == 357
