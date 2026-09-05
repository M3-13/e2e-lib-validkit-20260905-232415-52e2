"""Unit-Tests für die Telefonnummer-Normalisierung."""

import pytest

from validkit.phone import MAX_LENGTH, normalize_phone


def test_normalize_with_parentheses_spaces_hyphens() -> None:
    assert normalize_phone("(030) 123-4567", "49") == "+49301234567"


def test_normalize_strips_leading_zeros() -> None:
    assert normalize_phone("0301234567", "49") == "+49301234567"


def test_normalize_removes_all_non_digits() -> None:
    assert normalize_phone("(0)30-12 34/56", "49") == "+4930123456"


def test_single_digit_country_code() -> None:
    assert normalize_phone("2025550123", "1") == "+12025550123"


def test_three_digit_country_code() -> None:
    assert normalize_phone("1234567", "358") == "+3581234567"


def test_invalid_country_code_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("123", "x")


def test_empty_country_code_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("123", "")


def test_country_code_too_long_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("123", "1234")


def test_non_string_text_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone(123, "49")  # type: ignore[arg-type]


def test_non_string_country_code_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("123", 49)  # type: ignore[arg-type]


def test_no_digits_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("  ()- ", "49")


def test_only_zeros_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("000", "49")


def test_length_at_limit_is_allowed() -> None:
    result = normalize_phone("1" * MAX_LENGTH, "49")
    assert result == "+49" + "1" * MAX_LENGTH


def test_length_over_limit_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("1" * (MAX_LENGTH + 1), "49")


def test_error_message_does_not_contain_input() -> None:
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("(030) 123-4567", "x")
    assert "(030) 123-4567" not in str(exc_info.value)
