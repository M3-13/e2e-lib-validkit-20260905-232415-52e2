"""Unit-Tests für validkit.email.is_valid_email."""

import pytest

from validkit.email import is_valid_email


def test_valid_plain_address() -> None:
    assert is_valid_email("foo@bar.com") is True


def test_valid_case_insensitive() -> None:
    assert is_valid_email("FOO@BAR.COM") is True
    assert is_valid_email("Foo.Bar@Example.COM") is True


def test_valid_with_subdomain() -> None:
    assert is_valid_email("user@mail.example.com") is True


def test_valid_local_special_characters() -> None:
    assert is_valid_email("first.last@example.com") is True
    assert is_valid_email("user+tag@example.com") is True


def test_invalid_missing_domain() -> None:
    assert is_valid_email("foo@bar") is False


def test_invalid_whitespace() -> None:
    assert is_valid_email("foo bar.com") is False


def test_invalid_no_at_sign() -> None:
    assert is_valid_email("foobar.com") is False


def test_invalid_short_tld() -> None:
    assert is_valid_email("foo@bar.c") is False


def test_invalid_empty() -> None:
    assert is_valid_email("") is False


def test_wrong_type_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_email(123)  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        is_valid_email(None)  # type: ignore[arg-type]


def test_length_limit_raises_value_error() -> None:
    with pytest.raises(ValueError):
        is_valid_email("a" * 1001 + "@example.com")


def test_length_limit_at_boundary_is_checked() -> None:
    # Genau 1000 Zeichen ist gerade noch erlaubt und wird geprüft.
    assert is_valid_email("a" * 988 + "@example.com") is True


def test_error_message_does_not_contain_input() -> None:
    try:
        is_valid_email(123)  # type: ignore[arg-type]
    except ValueError as exc:
        assert "123" not in str(exc)

    secret = "secret@example.com" * 100
    try:
        is_valid_email(secret)
    except ValueError as exc:
        assert secret not in str(exc)
