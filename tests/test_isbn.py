"""Unit-Tests für die ISBN-13-Prüfung."""

import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_returns_true() -> None:
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_separators() -> None:
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces() -> None:
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit_returns_false() -> None:
    assert is_valid_isbn13("978-3-16-148410-7") is False


def test_wrong_check_digit_without_separators() -> None:
    assert is_valid_isbn13("9783161484101") is False


def test_too_short_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13("123")


def test_wrong_type_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13(9783161484100)


def test_none_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13(None)


def test_non_numeric_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13("978-3-16-148410-X")


def test_too_many_digits_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13("97831614841000")


def test_over_max_length_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_isbn13("9" * 1001)


def test_exact_max_length_is_not_rejected_by_length_limit() -> None:
    text = "9" * 1000
    with pytest.raises(ValueError):
        is_valid_isbn13(text)


def test_error_message_does_not_contain_input() -> None:
    secret = "978-3-16-148410-X"
    with pytest.raises(ValueError) as exc_info:
        is_valid_isbn13(secret)
    assert secret not in str(exc_info.value)
