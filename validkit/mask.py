"""Geheimnis-Maskierung."""


def mask_secret(text: str, keep: int = 4) -> str:
    """Maskiert ein Geheimnis und behält nur die letzten *keep* Zeichen.

    Args:
        text: Das zu maskierende Geheimnis.
        keep: Anzahl der vom Ende her sichtbar bleibenden Zeichen.

    Returns:
        Die maskierte Zeichenkette; ist *text* nicht länger als *keep*, wird
        *text* unverändert zurückgegeben.

    Raises:
        ValueError: Wenn *text* kein String ist oder *keep* negativ ist.
    """
    raise NotImplementedError
