"""Telefonnummer-Normalisierung."""


def normalize_phone(text: str, country_code: str) -> str:
    """Normalisiert eine Telefonnummer in das E.164-Format.

    Args:
        text: Die zu normalisierende Telefonnummer.
        country_code: Der Ländercode (ohne führendes Plus), z. B. ``"49"``.

    Returns:
        Die normalisierte Telefonnummer im Format ``+<country_code><number>``.

    Raises:
        ValueError: Wenn *text* kein String ist oder *country_code* kein gültiger
            Ländercode ist.
    """
    raise NotImplementedError
