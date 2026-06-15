from pydantic import BaseModel


class Record(BaseModel):
    active: bool
    count: int
    label: str


record = Record(active=True, count=5, label="x")
print(record.model_dump_json())
