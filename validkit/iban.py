"""IBAN-Validierung."""


def is_valid_iban(text: str) -> bool:
    """Prüft, ob *text* eine gültige IBAN ist.

    Args:
        text: Die zu prüfende IBAN (Leerzeichen werden ignoriert).

    Returns:
        True, wenn *text* eine gültige IBAN ist, sonst False.

    Raises:
        ValueError: Wenn *text* kein String ist oder zu kurz für eine IBAN ist.
    """
    raise NotImplementedError
