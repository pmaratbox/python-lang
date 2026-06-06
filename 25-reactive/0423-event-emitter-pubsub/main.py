from typing import Any, Callable, Dict, List

Handler = Callable[[Any], None]


class EventEmitter:
    def __init__(self) -> None:
        self._topics: Dict[str, List[Handler]] = {}

    def on(self, topic: str, handler: Handler) -> None:
        self._topics.setdefault(topic, []).append(handler)

    def emit(self, topic: str, payload: Any) -> None:
        for handler in list(self._topics.get(topic, [])):
            handler(payload)

    def off(self, topic: str, handler: Handler) -> None:
        handlers = self._topics.get(topic)
        if handlers is not None and handler in handlers:
            handlers.remove(handler)


def main() -> None:
    emitter = EventEmitter()

    def h(payload: Any) -> None:
        print("hi " + payload)

    def g(payload: Any) -> None:
        print("bye " + payload)

    emitter.on("greet", h)
    emitter.on("bye", g)

    emitter.emit("greet", "ada")
    emitter.emit("bye", "ada")

    emitter.off("greet", h)
    emitter.emit("greet", "x")


if __name__ == "__main__":
    main()
