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
    if not isinstance(text, str):
        raise ValueError("text muss ein String sein")
    if not isinstance(keep, int) or isinstance(keep, bool):
        raise ValueError("keep muss eine ganze Zahl sein")
    if keep < 0:
        raise ValueError("keep darf nicht negativ sein")
    if keep == 0:
        return "*" * len(text)
    if keep >= len(text):
        return text
    return "*" * (len(text) - keep) + text[-keep:]
