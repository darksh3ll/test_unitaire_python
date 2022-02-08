from main import adition, invert_chaine
import pytest


def test_adition_two_numbers():
    assert adition(12, 12) == 24


def test_reversed_chaine():
    assert invert_chaine("abc") == "Cba"
