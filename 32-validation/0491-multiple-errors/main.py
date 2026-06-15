from pydantic import BaseModel, Field, ValidationError


class MultipleErrors(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0, le=120)


def failing_fields(data: dict) -> str:
    try:
        MultipleErrors(**data)
    except ValidationError as err:
        # pydantic collects ALL errors by default (no fail-fast).
        fields = sorted({str(e["loc"][0]).lower() for e in err.errors()})
        return "\n".join(fields)
    return "ok"


if __name__ == "__main__":
    print(failing_fields({"name": "al", "age": 200}))
