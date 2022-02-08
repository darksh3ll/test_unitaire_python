from main import adition, invert_chaine, is_multiple_two,remove_consecutive_duplicates
import pytest


def test_adition_two_numbers():
    assert adition(12, 12) == 24


def test_reversed_chaine():
    assert invert_chaine("abc") == "Cba"


def test_array_contains_numbers_pair():
    assert is_multiple_two([1, 2, 3, 4, 5]) == [2, 4]


def test_remove_consecutive_duplicates():
    enter ="alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    exit = "alpha beta gamma delta alpha beta gamma delta"
    assert remove_consecutive_duplicates(enter) == exit
