"""Luhn-Prüfsummen-Validierung."""


def luhn_check(digits: str) -> bool:
    """Prüft eine Ziffernfolge gegen die Luhn-Prüfsumme.

    Args:
        digits: Die zu prüfende Ziffernfolge (nur Ziffern).

    Returns:
        True, wenn die Prüfsumme gültig ist, sonst False.

    Raises:
        ValueError: Wenn *digits* kein String ist, nicht ausschließlich Ziffern
            enthält oder zu kurz ist.
    """
    raise NotImplementedError
