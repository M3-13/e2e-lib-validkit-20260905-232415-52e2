"""Diakritika-Entfernung."""

import unicodedata


def strip_accents(text: str) -> str:
    """Entfernt diakritische Zeichen (Akzente) aus *text*.

    Args:
        text: Die zu bereinigende Zeichenkette.

    Returns:
        *text* ohne diakritische Zeichen, z. B. ``"café"`` -> ``"cafe"``.

    Raises:
        ValueError: Wenn *text* kein String ist.
    """
    if not isinstance(text, str):
        raise ValueError("strip_accents erwartet eine Zeichenkette")

    decomposed = unicodedata.normalize("NFD", text)
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")
