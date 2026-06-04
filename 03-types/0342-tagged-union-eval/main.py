from dataclasses import dataclass
from typing import Union


@dataclass
class Num:
    value: int


@dataclass
class Add:
    left: "Expr"
    right: "Expr"


Expr = Union[Num, Add]


def eval_expr(e: Expr) -> int:
    if isinstance(e, Num):
        return e.value
    if isinstance(e, Add):
        return eval_expr(e.left) + eval_expr(e.right)
    raise TypeError("unknown expr")


print(eval_expr(Add(Num(1), Num(2))))
