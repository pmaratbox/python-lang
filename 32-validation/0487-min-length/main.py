from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0, le=120)


try:
    User(name="al", age=30)
    print("ok")
except ValidationError as e:
    print("\n".join(sorted({str(err["loc"][0]).lower() for err in e.errors()})))
