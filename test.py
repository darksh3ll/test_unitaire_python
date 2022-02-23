from main import adition, \
    invert_chaine, \
    is_multiple_two, \
    remove_consecutive_duplicates, is_palindrome, get_sum_of_digits, duplicate_elements, valid_spacing
import pytest


@pytest.mark.parametrize("a,b, expected_result", [
    (12, 12, 24), (1, 1, 2), (10, 5, 15), (-10, -5, -15)

])
def test_adition_two_numbers(a, b, expected_result):
    assert adition(a, b) == expected_result


def test_reversed_chaine():
    assert invert_chaine("abc") == "Cba"


def test_array_contains_numbers_pair():
    assert is_multiple_two([1, 2, 3, 4, 5]) == [2, 4]


def test_remove_consecutive_duplicates():
    enter = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    exit = "alpha beta gamma delta alpha beta gamma delta"
    assert remove_consecutive_duplicates(enter) == exit


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("abc", False),
    ("abab", False),
    ("kayak", True),
    (123, None),
])
def test_is_palidrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("123", 6),
    ("223", 7),
    ("aaa", None),
])
def test_get_sum_of_digits(string, expected_result):
    assert get_sum_of_digits(string) == expected_result


def test_duplicate_elements():
    assert duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]) == True


@pytest.mark.parametrize("string, expected_result", [
    ('Hello world', True),
    ('Hello world ', False),
])
def test_valid_spacing(string, expected_result):
    assert valid_spacing(string) == expected_result
