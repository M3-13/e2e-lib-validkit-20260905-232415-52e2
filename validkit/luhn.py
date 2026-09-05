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
    if not isinstance(digits, str):
        raise ValueError("luhn_check erwartet einen String aus Ziffern")

    if len(digits) < 2:
        raise ValueError("Ziffernfolge muss mindestens zwei Ziffern enthalten")

    if not digits.isdigit():
        raise ValueError("Ziffernfolge darf nur Ziffern enthalten")

    total = 0
    for index, char in enumerate(reversed(digits)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
