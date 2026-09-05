"""Unit-Tests für die IBAN-Validierung."""

import pytest

from validkit.iban import is_valid_iban


def test_valid_iban_with_spaces() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_lowercase() -> None:
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


def test_valid_iban_compact() -> None:
    assert is_valid_iban("DE89370400440532013000") is True


def test_other_country_valid_iban() -> None:
    assert is_valid_iban("GB82WEST12345698765432") is True


def test_changed_checksum_is_false() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_wrong_country_code_is_false() -> None:
    assert is_valid_iban("1E89 3704 0044 0532 0130 00") is False


def test_non_alphanumeric_is_false() -> None:
    assert is_valid_iban("DE89-3704-0044-0532-0130-00") is False


def test_too_short_iban_is_false() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704")


def test_too_long_iban_is_false() -> None:
    assert is_valid_iban("DE89" + "0" * 40) is False


def test_too_short_iban_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("DE")


def test_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("")


def test_wrong_type_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban(12345)


def test_none_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban(None)


def test_over_length_limit_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_iban("A" * 1001)


def test_length_limit_boundary_is_accepted() -> None:
    assert is_valid_iban("A" * 1000) is False
