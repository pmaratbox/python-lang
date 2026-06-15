# 0538 — Sequence

Use the `parsy` parser-combinator library: the `seq` combinator runs `string("a")` and then `string("b")` in order, collecting both results, and `.map("".join)` combines them into the single string `ab`. Parsing the fixed input `ab` prints the combined result.

## Run

    python3 main.py
