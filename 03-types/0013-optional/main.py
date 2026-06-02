from typing import Optional

present: Optional[int] = 42
absent: Optional[int] = None

print(f"present: {present if present is not None else -1}")
print(f"absent: {absent if absent is not None else -1}")
