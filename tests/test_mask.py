"""Unit-Tests für validkit.mask.mask_secret."""

import pytest

from validkit.mask import mask_secret


def test_keep_masks_all_but_last_four() -> None:
    assert mask_secret("geheim123", 4) == "*****m123"


def test_default_keep_value_is_four() -> None:
    assert mask_secret("geheim123") == "*****m123"


def test_keep_greater_than_text_length_returns_text_unchanged() -> None:
    assert mask_secret("abc", 5) == "abc"


def test_keep_equal_to_text_length_returns_text_unchanged() -> None:
    assert mask_secret("abc", 3) == "abc"


def test_keep_zero_masks_every_character() -> None:
    assert mask_secret("abc", 0) == "***"


def test_empty_text_with_keep_zero() -> None:
    assert mask_secret("", 0) == ""


def test_negative_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("abc", -1)


def test_non_string_text_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret(123)  # type: ignore[arg-type]


def test_non_int_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("abc", "4")  # type: ignore[arg-type]


def test_bool_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("abc", True)  # type: ignore[arg-type]


def test_error_message_does_not_contain_input() -> None:
    secret = "topsecretvalue"
    with pytest.raises(ValueError) as exc_info:
        mask_secret(secret, -1)
    assert secret not in str(exc_info.value)
