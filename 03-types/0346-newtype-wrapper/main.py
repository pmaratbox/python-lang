from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: int

    def __str__(self) -> str:
        return "user-{}".format(self.value)


@dataclass(frozen=True)
class ProductId:
    value: int

    def __str__(self) -> str:
        return "prod-{}".format(self.value)


u = UserId(1)
p = ProductId(2)
print("{} {}".format(u, p))
