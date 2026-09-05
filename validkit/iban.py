"""IBAN-Validierung."""

import re

# Maximale Eingabelänge, die vor der Regex-Prüfung akzeptiert wird.
_MAX_LENGTH = 1000

_IBAN_RE = re.compile(r"[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}")


def is_valid_iban(text: str) -> bool:
    """Prüft, ob *text* eine gültige IBAN ist.

    Leerzeichen und Groß-/Kleinschreibung werden normalisiert; die Prüfung
    umfasst das Grundformat (zwei Buchstaben, zwei Ziffern, alphanumerischer
    Rest), die Gesamtlänge (15 bis 34 Zeichen) und das Modulo-97-Verfahren.

    Args:
        text: Die zu prüfende IBAN (Leerzeichen werden ignoriert).

    Returns:
        True, wenn *text* eine gültige IBAN ist, sonst False.

    Raises:
        ValueError: Wenn *text* kein String ist, zu kurz für eine IBAN ist
            oder die Maximallänge von 1000 Zeichen überschreitet.
    """
    if not isinstance(text, str):
        raise ValueError("invalid type: expected str")
    if len(text) > _MAX_LENGTH:
        raise ValueError("input exceeds maximum length")

    normalized = text.replace(" ", "").upper()
    if len(normalized) < 15:
        raise ValueError("input is too short for an IBAN")
    if not _IBAN_RE.fullmatch(normalized):
        return False

    rearranged = normalized[4:] + normalized[:4]
    numeric = "".join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged)
    return int(numeric) % 97 == 1
