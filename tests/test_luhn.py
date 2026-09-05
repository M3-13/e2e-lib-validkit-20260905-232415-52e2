"""Unit-Tests für validkit.luhn."""

import pytest

from validkit.luhn import luhn_check


def test_valid_checksum() -> None:
    assert luhn_check("79927398713") is True


def test_invalid_checksum() -> None:
    assert luhn_check("79927398712") is False


def test_minimal_two_digits_valid() -> None:
    assert luhn_check("00") is True


def test_single_digit_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("7")


def test_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("")


def test_non_digit_character_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("12a")


def test_wrong_type_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check(79927398713)  # type: ignore[arg-type]


def test_none_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check(None)  # type: ignore[arg-type]


def test_error_message_does_not_contain_input() -> None:
    for bad in ("12a", "7", "79927398712a"):
        with pytest.raises(ValueError) as exc_info:
            luhn_check(bad)
        assert bad not in str(exc_info.value)
