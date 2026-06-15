from transitions import Machine


class Process:
    pass


process = Process()
Machine(
    model=process,
    states=["idle", "running"],
    initial="idle",
    transitions=[
        {"trigger": "start", "source": "idle", "dest": "running"},
        {"trigger": "reset", "source": "running", "dest": "idle"},
    ],
)

process.start()
process.reset()

print(process.state.lower())
