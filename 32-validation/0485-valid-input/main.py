from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0, le=120)


try:
    Person(name="alice", age=30)
    print("ok")
except ValidationError as err:
    fields = sorted({str(e["loc"][0]) for e in err.errors()})
    print("\n".join(fields))
