from typing import Callable, Dict


def observablecreate(observer: Dict[str, Callable]) -> None:
    observer["next"](1)
    observer["next"](2)
    observer["next"](3)
    observer["complete"]()


def main() -> None:
    observer = {
        "next": lambda value: print(value),
        "complete": lambda: print("done"),
    }
    observablecreate(observer)


if __name__ == "__main__":
    main()
