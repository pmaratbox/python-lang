# 0533 — Map & filter

Use the `pyrsistent` persistent collection library: starting from a `pvector([1, 2, 3, 4, 5])`, filter the even numbers into a new vector, then `.transform` each surviving element by multiplying it by 10. Both the filter and the `.transform` map RETURN A NEW immutable vector rather than mutating in place, so the original is left unchanged. Printing the result space-joined yields `20 40`.

## Run

    python3 main.py
