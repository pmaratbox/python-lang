class BaseError(Exception):
    pass


class SpecificError(BaseError):
    pass


try:
    raise SpecificError("boom")
except BaseError:
    print("caught base")
