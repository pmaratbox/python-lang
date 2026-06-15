# 0539 — Alternative

Use the `parsy` parser-combinator library and its alternative/choice combinator (`|`): the parser `string("cat") | string("dog")` tries the first parser and, if it fails, falls back to the second. Running it on the fixed input `"dog"` selects the second branch and yields `dog`.

## Run

    python3 main.py
