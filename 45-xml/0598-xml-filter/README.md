# 0598 — Filter by attribute

Uses Python's standard-library `xml.etree.ElementTree` to parse a fixed catalog document and filter `<book>` elements by attribute, keeping only those whose `lang` attribute equals `en` (just `b1`) via the ElementTree XPath subset, then joining their `<title>` text with commas (`Go`).

## Run

    python3 main.py
