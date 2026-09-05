# validkit

Eine kleine, eigenständige Python-Bibliothek ohne externe Laufzeit-Abhängigkeiten,
die neun unabhängige, reine, typannotierte Funktionen für Validierung und
Normalisierung bereitstellt. Alle Funktionen werden über `validkit/__init__.py`
exportiert und sind als `from validkit import ...` nutzbar.

## Tech-Stack

- **Sprache**: Python
- **Runtime**: Python 3.10+
- **Testing**: pytest (nur Dev-Abhängigkeit)
- **Paketierung**: setuptools / `pyproject.toml`
- **Abhängigkeiten**: keine (Standardbibliothek)

## Installation

```bash
pip install -e .[dev]
```

## Tests ausführen

```bash
pytest
```

## Funktionen und Beispiele

Jede der neun Funktionen ist im Folgenden mit genau einem kurzen,
ausführbaren Beispiel samt erwartetem Ergebnis dokumentiert. Alle Werte sind
synthetisch.

### `is_valid_email(text: str) -> bool`

```python
from validkit import is_valid_email

is_valid_email("foo@bar.com")  # True
```

### `luhn_check(digits: str) -> bool`

```python
from validkit import luhn_check

luhn_check("79927398713")  # True
```

### `is_valid_iban(text: str) -> bool`

```python
from validkit import is_valid_iban

is_valid_iban("DE89 3704 0044 0532 0130 00")  # True
```

### `is_valid_isbn13(text: str) -> bool`

```python
from validkit import is_valid_isbn13

is_valid_isbn13("978-3-16-148410-0")  # True
```

### `normalize_phone(text: str, country_code: str) -> str`

```python
from validkit import normalize_phone

normalize_phone("(030) 123-4567", "49")  # '+49301234567'
```

### `strip_accents(text: str) -> str`

```python
from validkit import strip_accents

strip_accents("café résumé")  # 'cafe resume'
```

### `mask_secret(text: str, keep: int = 4) -> str`

```python
from validkit import mask_secret

mask_secret("geheim123", 4)  # '*****0123'
```

### `slugify(text: str) -> str`

```python
from validkit import slugify

slugify("Héllo Wörld!")  # 'hello-world'
```

### `clamp(value, low, high) -> int | float`

```python
from validkit import clamp

clamp(5, 0, 10)  # 5
```
