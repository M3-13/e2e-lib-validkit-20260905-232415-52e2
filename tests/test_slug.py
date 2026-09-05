"""Unit-Tests für die Slug-Erzeugung."""

import pytest

from validkit.slug import slugify


def test_slugify_removes_accents() -> None:
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_lowercases_and_hyphenates_spaces() -> None:
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_special_characters() -> None:
    assert slugify("Foo & Bar") == "foo-bar"


def test_slugify_collapses_multiple_hyphens() -> None:
    assert slugify("a--b__c") == "a-b-c"


def test_slugify_strips_leading_and_trailing_hyphens() -> None:
    assert slugify("---hello---") == "hello"


def test_slugify_handles_only_alphanumeric_input() -> None:
    assert slugify("abc123") == "abc123"


def test_slugify_no_usable_characters_raises() -> None:
    with pytest.raises(ValueError):
        slugify("!!!")


def test_slugify_empty_string_raises() -> None:
    with pytest.raises(ValueError):
        slugify("")


def test_slugify_wrong_type_raises() -> None:
    with pytest.raises(ValueError):
        slugify(123)  # type: ignore[arg-type]


def test_slugify_none_raises() -> None:
    with pytest.raises(ValueError):
        slugify(None)  # type: ignore[arg-type]


def test_slugify_rejects_input_over_max_length() -> None:
    with pytest.raises(ValueError):
        slugify("a" * 1001)


def test_slugify_accepts_input_at_max_length() -> None:
    assert slugify("a" * 1000) == "a" * 1000
