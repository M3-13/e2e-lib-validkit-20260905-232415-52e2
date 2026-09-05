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
        ValueError: Wenn *low* größer als *high* ist oder ein Argument weder
            ``int`` noch ``float`` ist.
    """
    for name, arg in (("value", value), ("low", low), ("high", high)):
        if isinstance(arg, bool) or not isinstance(arg, (int, float)):
            raise ValueError(f"{name} must be an int or float")

    if low > high:
        raise ValueError("low must not be greater than high")

    if value < low:
        return low
    if value > high:
        return high
    return value
