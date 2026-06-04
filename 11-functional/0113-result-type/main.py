from collections import namedtuple

Ok = namedtuple("Ok", ["value"])
Err = namedtuple("Err", ["msg"])


def safe_div(a, b):
    if b == 0:
        return Err("divide by zero")
    return Ok(a // b)


def show(r):
    if isinstance(r, Ok):
        print("ok: {}".format(r.value))
    else:
        print("err: {}".format(r.msg))


show(safe_div(10, 2))
show(safe_div(1, 0))
