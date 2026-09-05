"""Import-Smoke-Tests für das validkit-Paket."""

import validkit


def test_all_public_names_importable() -> None:
    names = [
        "is_valid_email",
        "luhn_check",
        "is_valid_iban",
        "is_valid_isbn13",
        "normalize_phone",
        "strip_accents",
        "mask_secret",
        "slugify",
        "clamp",
    ]
    for name in names:
        assert hasattr(validkit, name)


def test_public_api_exports_all_names() -> None:
    expected = {
        "is_valid_email",
        "luhn_check",
        "is_valid_iban",
        "is_valid_isbn13",
        "normalize_phone",
        "strip_accents",
        "mask_secret",
        "slugify",
        "clamp",
    }
    assert set(validkit.__all__) == expected
