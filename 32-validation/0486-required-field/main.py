from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=120)


# Input has name present but the required field "age" is MISSING.
data = {"name": "ada"}

try:
    Person(**data)
    print("ok")
except ValidationError as err:
    fields = sorted({str(e["loc"][0]) for e in err.errors()})
    print("\n".join(f.lower() for f in fields))
