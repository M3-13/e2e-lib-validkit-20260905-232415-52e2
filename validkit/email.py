"""E-Mail-Validierung."""

import re

# Maximale akzeptierte Eingabelänge, bevor die Regex-Prüfung ausgeführt wird.
# Eingaben oberhalb dieser Grenze werden mit ValueError abgelehnt, um
# DoS über überlange Zeichenketten zu vermeiden (AC-15).
_MAX_LENGTH = 1000

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def is_valid_email(text: str) -> bool:
    """Prüft, ob *text* eine syntaktisch gültige E-Mail-Adresse ist.

    Pragmatische, rein formatbasierte Prüfung ohne Netzwerk- oder
    DNS-Aufrufe: lokaler Teil, ``@``, Domain mit Punkt und einem TLD-Muster
    aus mindestens zwei Buchstaben. Die Prüfung ist case-insensitive.

    Eingaben mit mehr als 1000 Zeichen werden vor der Regex-Prüfung mit
    ``ValueError`` abgelehnt.

    Args:
        text: Die zu prüfende Zeichenkette.

    Returns:
        True, wenn *text* eine gültige E-Mail-Adresse ist, sonst False.

    Raises:
        ValueError: Wenn *text* kein String ist oder die Maximallänge von
            1000 Zeichen überschreitet.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if len(text) > _MAX_LENGTH:
        raise ValueError("input exceeds maximum allowed length")
    return _EMAIL_RE.match(text) is not None
