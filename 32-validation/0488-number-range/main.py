from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0, le=120)


try:
    User(name="alice", age=200)
    print("ok")
except ValidationError as e:
    print("\n".join(sorted({str(err["loc"][0]) for err in e.errors()})))
