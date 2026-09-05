"""Diakritika-Entfernung."""


def strip_accents(text: str) -> str:
    """Entfernt diakritische Zeichen (Akzente) aus *text*.

    Args:
        text: Die zu bereinigende Zeichenkette.

    Returns:
        *text* ohne diakritische Zeichen, z. B. ``"café"`` -> ``"cafe"``.

    Raises:
        ValueError: Wenn *text* kein String ist.
    """
    raise NotImplementedError
