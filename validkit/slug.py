"""Slug-Erzeugung."""


def slugify(text: str) -> str:
    """Erzeugt einen URL-tauglichen Slug aus *text*.

    Args:
        text: Die zu konvertierende Zeichenkette.

    Returns:
        Einen Slug in Kleinbuchstaben, z. B. ``"Héllo Wörld!"`` ->
        ``"hello-world"``.

    Raises:
        ValueError: Wenn *text* kein String ist oder keine verwertbaren Zeichen
            enthält.
    """
    raise NotImplementedError
