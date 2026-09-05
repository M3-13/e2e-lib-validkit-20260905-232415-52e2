VERDICT: CHANGES_REQUESTED

## Prüfbericht validkit (Merge-Stand)

**Projekttyp:** reine Python-Bibliothek ohne Endnutzer-UI.  
**Geprüfte Regulierung:** DSGVO, EU Cyber Resilience Act (CRA).  
**Nicht anwendbar:** EU AI Act (keine KI-Funktion), Impressum/AGB/Datenschutzerklärung/Cookie-Banner (keine öffentliche Web-UI), Barrierefreiheit WCAG/BITV/EAA (keine Web-UI).

---

## 1. DSGVO / Datenschutz

### 1.1 Positivbefund: Keine Speicherung, keine Protokollierung, keine Weitergabe
Die Bibliothek ist rein funktional. Im sichtbaren Code gibt es weder Logging, noch Persistenz, noch Netzwerkaufrufe. Die Funktionen verarbeiten übergebene Werte ausschließlich im Arbeitsspeicher und geben Ergebnisse zurück. Eine eigene datenschutzrechtliche Verantwortlichkeit der Bibliothek entsteht insoweit nicht; die DSGVO-Pflichten treffen den Integrator/Betreiber.

### 1.2 Positivbefund: Keine personenbezogenen Daten in Fehlermeldungen
Alle `ValueError`-Meldungen sind generisch formuliert und enthalten keine Eingabewerte. Dies ist durch die Tests (`test_error_message_does_not_contain_input*`) abgesichert. Beispiele:
- `validkit/email.py`: `"input exceeds maximum allowed length"`
- `validkit/iban.py`: `"input is too short for an IBAN"`
- `validkit/luhn.py`: `"Ziffernfolge darf nur Ziffern enthalten"`

### 1.3 Positivbefund: Synthetische Testdaten
Die sichtbaren Tests verwenden ausschließlich synthetische/fiktive Werte (`foo@bar.com`, `DE89 3704 0044 0532 0130 00`, `geheim123`, `978-3-16-148410-0`). AC-17 ist erfüllt.

### 1.4 Befund — mittel: `luhn_check` ohne Eingabelängenlimit
**Schweregrad:** medium

`luhn_check` validiert typischerweise Kreditkartennummern/PANs, also besonders schützenswerte Zahlungsdaten. Die Funktion besitzt als einzige zahlungsdatenverarbeitende Funktion **kein** Längenlimit und iteriert über die gesamte Eingabe. Bei sehr langen Eingaben kann dies zu unnötig langer CPU-Last führen und die in den übrigen Funktionen einheitlich umgesetzte DoS-Abwehr unterlaufen.

**Abhilfe:** In `validkit/luhn.py` eine Maximallänge analog zu den anderen Modulen einführen:

```python
_MAX_LENGTH = 1000

def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise ValueError("luhn_check erwartet einen String aus Ziffern")
    if len(digits) > _MAX_LENGTH:
        raise ValueError("input exceeds maximum length")
    ...
```

Die Fehlermeldung bleibt generisch und enthält keine Eingabedaten. Dies bricht keine sichtbaren Tests und erhält die Funktion für alle praxisüblichen Kartennummern.

### 1.5 Befund — niedrig: `strip_accents` ohne Eingabelängenlimit
**Schweregrad:** low

`strip_accents` normalisiert und iteriert über die gesamte Eingabe ohne Längenbegrenzung. Zwar ist dies weniger kritisch als bei Zahlungsdaten, aber aus Konsistenzgründen und zur einheitlichen Ressourcenbegrenzung sollte auch hier ein Limit existieren.

**Abhilfe:** In `validkit/accents.py` `_MAX_LENGTH = 1000` definieren und vor der Normalisierung prüfen, z. B.:

```python
if len(text) > _MAX_LENGTH:
    raise ValueError("text exceeds maximum length")
```

---

## 2. EU Cyber Resilience Act (CRA)

### 2.1 Positivbefund: Sicherer Code ohne dynamische Ausführung
Im gesamten Paket sind keine Aufrufe von `eval`, `exec`, `compile` oder `pickle.loads` sichtbar. AC-13 ist erfüllt.

### 2.2 Positivbefund: Keine ReDoS-anfälligen regulären Ausdrücke
Alle sichtbaren regulären Ausdrücke vermeiden verschachtelte Quantoren:
- `email.py`: `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
- `iban.py`: `[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}`
- `isbn.py`: `^\d{13}$`
- `phone.py`: `^\d{1,3}$` und `\D`
- `slug.py`: `[^a-z0-9]+`

AC-14 ist erfüllt. Die regexbasierten Funktionen (`email`, `iban`, `isbn`, `phone`, `slug`) lehnen Eingaben über 1000 Zeichen vor der Regex-Prüfung ab. AC-15 ist für die regexbasierten Funktionen erfüllt.

### 2.3 Positivbefund: Keine Laufzeitabhängigkeiten / minimale SBOM
`pyproject.toml` deklariert `dependencies = []`. Damit ist das Supply-Chain-Risiko minimal und die Abhängigkeitsliste ist transparent. Dies genügt als einfache SBOM für ein Paket ohne Fremdabhängigkeiten.

### 2.4 Befund — mittel: CRA-Sicherheitsdokumentation nicht sichtbar
**Schweregrad:** medium

Für Produkte mit digitalen Elementen verlangt der CRA dokumentierte Sicherheitseigenschaften sowie Angaben zu Sicherheitsupdates und Schwachstellenmeldungen. Im sichtbaren Stand sind solche Angaben weder in `README.md` noch in einer `SECURITY.md` erkennbar. Die Spec (AC-12) sieht für `README.md` nur je ein Funktionsbeispiel vor.

**Abhilfe:** In `README.md` einen Abschnitt **„Sicherheit & Wartung (CRA)“** ergänzen, mindestens mit:
- Eingabelängenlimits aller öffentlichen Funktionen (nach Umsetzung von 1.4/1.5)
- Aussage: keine Laufzeitabhängigkeiten, keine dynamische Codeausführung
- unterstützte Python-Version (`>=3.10`)
- Prozess für Sicherheitsupdates (Release-/Versionsschema)
- Meldestelle für Schwachstellen (z. B. E-Mail-Adresse oder Issue-Template)

Alternativ kann eine separate `SECURITY.md` im Repository ergänzt werden.

### 2.5 Befund — niedrig: Update-/Patchfähigkeit nicht explizit dokumentiert
**Schweregrad:** low

Das Paket ist über `setuptools`/`pyproject.toml` versioniert (`0.1.0`) und damit grundsätzlich aktualisierbar. Eine kurze Aussage zu Updateprozess und Versionspolitik fehlt jedoch.

**Abhilfe:** In den CRA-Abschnitt der README aufnehmen: „Updates erfolgen über die Paketregistrierung; Sicherheitsrelevante Korrekturen werden mit einer neuen Patchversion veröffentlicht.“

---

## 3. EU AI Act

Nicht anwendbar. Es ist keine KI-Funktion im Produkt sichtbar.

---

## 4. Pflichttexte & UI-Pflichten

Nicht anwendbar. Es gibt keine öffentliche Web-UI, keine Cookies, keine Verkaufs- oder Registrierungsstrecke. Daher bestehen keine Pflichten zu Impressum, AGB, Datenschutzerklärung, Cookie-Banner oder Widerrufsbelehrung.

---

## 5. Barrierefreiheit

Nicht anwendbar. Keine Endnutzer-UI, keine Webinhalte.

---

## Gesamtfazit

Der Merge-Stand ist grundsätzlich datenschutzfreundlich und sicher umgesetzt. Es bestehen **keine fundamentalen Rechtsverstöße**. Offen sind behebbare Lücken:

1. Fehlendes Eingabelängenlimit bei `luhn_check` (mittel) und `strip_accents` (niedrig).
2. Nicht sichtbare CRA-Sicherheitsdokumentation in `README.md`/`SECURITY.md` (mittel).
3. Fehlende explizite Update-/Patchdokumentation (niedrig).

Diese können ohne Bruch bestehender Produktfunktionen behoben werden. Daher: **CHANGES_REQUESTED**.