# 0027 — File I/O

Write `hello, file` to a file, read it back, delete the file, and print `read: hello, file`. `open(path, "w")` then `open(path)` inside `with` blocks guarantee the file is closed even on error; `f.write`/`f.read` transfer the text and `os.remove` deletes it. The default mode is text, so no encoding juggling is needed.

## Run

    python3 main.py
