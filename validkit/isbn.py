"""ISBN-13-Prüfung."""

import re

_MAX_LENGTH = 1000

_DIGITS_RE = re.compile(r"^\d{13}$")


def is_valid_isbn13(text: str) -> bool:
    """Prüft, ob *text* eine gültige ISBN-13 ist.

    Vor der Prüfung werden Trennzeichen (Bindestriche und Leerzeichen)
    entfernt. Die Prüfung besteht aus 13 Ziffern, deren letzte die
    Prüfziffer nach dem ISBN-13-Verfahren (Gewichtung 1/3 alternierend)
    ist.

    Args:
        text: Die zu prüfende ISBN-13 (Bindestriche und Leerzeichen werden
            ignoriert). Die maximale Länge der Eingabe beträgt 1.000 Zeichen.

    Returns:
        True, wenn *text* eine gültige ISBN-13 ist, sonst False.

    Raises:
        ValueError: Wenn *text* kein String ist, zu kurz ist, nicht nur aus
            Ziffern und Trennzeichen besteht oder länger als 1.000 Zeichen
            ist.
    """
    if not isinstance(text, str):
        raise ValueError("ISBN muss eine Zeichenkette sein")
    if len(text) > _MAX_LENGTH:
        raise ValueError("ISBN überschreitet die maximale Länge")

    digits = re.sub(r"[-\s]", "", text)
    if not _DIGITS_RE.match(digits):
        raise ValueError("ISBN muss aus 13 Ziffern bestehen")

    total = sum(
        int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits[:12])
    )
    check_digit = (10 - total % 10) % 10
    return check_digit == int(digits[12])
