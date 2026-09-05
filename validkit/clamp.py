"""Clamp-Funktion."""


def clamp(value: int | float, low: int | float, high: int | float) -> int | float:
    """Begrenzt *value* auf das Intervall [*low*, *high*].

    Args:
        value: Der zu begrenzende Wert.
        low: Untere Grenze.
        high: Obere Grenze.

    Returns:
        *low*, wenn *value* kleiner als *low* ist; *high*, wenn *value* größer
        als *high* ist; sonst *value*.

    Raises:
        ValueError: Wenn *low* größer als *high* ist.
    """
    raise NotImplementedError
