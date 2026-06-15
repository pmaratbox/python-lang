from pydantic import BaseModel, Field, ValidationError


class M(BaseModel):
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


try:
    M(email="not-an-email")
    print("ok")
except ValidationError as e:
    print("\n".join(sorted({str(err["loc"][0]) for err in e.errors()})))
