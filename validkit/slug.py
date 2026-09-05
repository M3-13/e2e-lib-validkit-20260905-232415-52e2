"""Slug-Erzeugung."""

import re
import unicodedata

_MAX_LENGTH = 1000


def slugify(text: str) -> str:
    """Erzeugt einen URL-tauglichen Slug aus *text*.

    Der Slug besteht ausschließlich aus Kleinbuchstaben (a-z) und Ziffern
    (0-9); alle übrigen Zeichen werden zu ``-``. Diakritische Zeichen werden
    mittels Unicode-NFD-Normalisierung entfernt, aufeinanderfolgende
    Bindestriche werden kollabiert und führende/folgende Bindestriche entfernt.

    Args:
        text: Die zu konvertierende Zeichenkette.

    Returns:
        Einen Slug in Kleinbuchstaben, z. B. ``"Héllo Wörld!"`` ->
        ``"hello-world"``.

    Raises:
        ValueError: Wenn *text* kein String ist, keine verwertbaren Zeichen
            enthält oder länger als 1000 Zeichen ist.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if len(text) > _MAX_LENGTH:
        raise ValueError("text exceeds maximum length of 1000 characters")

    normalized = unicodedata.normalize("NFD", text)
    stripped = "".join(c for c in normalized if unicodedata.category(c) != "Mn")
    lowered = stripped.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    if not slug:
        raise ValueError("text contains no usable characters")
    return slug
