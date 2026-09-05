"""Telefonnummer-Normalisierung.

Eingaben mit mehr als ``MAX_LENGTH`` (1000) Zeichen werden vor jeder
Regex-Verarbeitung abgelehnt.
"""

import re

MAX_LENGTH = 1000

_COUNTRY_CODE_RE = re.compile(r"^\d{1,3}$")
_NON_DIGIT_RE = re.compile(r"\D")


def normalize_phone(text: str, country_code: str) -> str:
    """Normalisiert eine Telefonnummer in das E.164-Format.

    Args:
        text: Die zu normalisierende Telefonnummer.
        country_code: Der Ländercode (ohne führendes Plus), z. B. ``"49"``.

    Returns:
        Die normalisierte Telefonnummer im Format ``+<country_code><number>``.

    Raises:
        ValueError: Wenn *text* oder *country_code* kein String ist, wenn der
            Ländercode nicht aus 1 bis 3 Ziffern besteht, wenn *text* keine
            Ziffern enthält oder wenn *text* die Maximallänge ``MAX_LENGTH``
            (1000 Zeichen) überschreitet.
    """
    if not isinstance(text, str):
        raise ValueError("text muss ein String sein")
    if not isinstance(country_code, str):
        raise ValueError("country_code muss ein String sein")
    if len(text) > MAX_LENGTH:
        raise ValueError("Eingabe überschreitet die Maximallänge")
    if not _COUNTRY_CODE_RE.fullmatch(country_code):
        raise ValueError("Ländercode muss aus 1 bis 3 Ziffern bestehen")
    digits = _NON_DIGIT_RE.sub("", text).lstrip("0")
    if not digits:
        raise ValueError("Telefonnummer enthält keine Ziffern")
    return f"+{country_code}{digits}"
