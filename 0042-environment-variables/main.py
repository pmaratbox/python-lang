import os

value = os.environ.get("LESSON_ENV_VAR", "default")
print(f"value: {value}")
