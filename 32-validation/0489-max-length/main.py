from pydantic import BaseModel, Field, ValidationError


class M(BaseModel):
    code: str = Field(max_length=5)


try:
    M(code="ABCDEFG")
    print("ok")
except ValidationError as e:
    print("\n".join(sorted({str(err["loc"][0]) for err in e.errors()})))
