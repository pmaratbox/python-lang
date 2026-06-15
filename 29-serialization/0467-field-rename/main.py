from pydantic import BaseModel, Field


class Person(BaseModel):
    fullName: str = Field(serialization_alias="full_name")


print(Person(fullName="alice").model_dump_json(by_alias=True))
