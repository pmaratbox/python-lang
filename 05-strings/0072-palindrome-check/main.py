for word in ("level", "hello"):
    is_pal = word == word[::-1]
    print(f"{word}: {'yes' if is_pal else 'no'}")
