from pydantic import TypeAdapter

numbers = TypeAdapter(list[int])
print(numbers.dump_json([1, 2, 3]).decode())
