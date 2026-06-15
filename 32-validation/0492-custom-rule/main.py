from pydantic import BaseModel, field_validator, ValidationError


class CustomRule(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def must_contain_digit(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("must contain at least one digit")
        return v


try:
    CustomRule(password="abcdef")
    print("ok")
except ValidationError as err:
    fields = sorted({str(e["loc"][0]) for e in err.errors()})
    print("\n".join(f.lower() for f in fields))
