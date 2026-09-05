"""ISBN-13-Prüfung."""


def is_valid_isbn13(text: str) -> bool:
    """Prüft, ob *text* eine gültige ISBN-13 ist.

    Args:
        text: Die zu prüfende ISBN-13 (Bindestriche werden ignoriert).

    Returns:
        True, wenn *text* eine gültige ISBN-13 ist, sonst False.

    Raises:
        ValueError: Wenn *text* kein String ist oder nicht die erforderliche
            Länge hat.
    """
    raise NotImplementedError
