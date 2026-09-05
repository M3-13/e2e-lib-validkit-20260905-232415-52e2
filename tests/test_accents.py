"""Tests für validkit.accents."""

import pytest

from validkit.accents import strip_accents


def test_multiple_accents():
    assert strip_accents("café résumé") == "cafe resume"


def test_german_umlauts():
    assert strip_accents("grüße") == "gruße"
    assert strip_accents("äöü") == "aou"


def test_text_without_accents_unchanged():
    assert strip_accents("hello world 123") == "hello world 123"


def test_combining_character_removed():
    assert strip_accents("e\u0301") == "e"
    assert strip_accents("a\u0308") == "a"


def test_empty_string():
    assert strip_accents("") == ""


def test_wrong_type_raises_value_error():
    with pytest.raises(ValueError):
        strip_accents(123)
    with pytest.raises(ValueError):
        strip_accents(None)
