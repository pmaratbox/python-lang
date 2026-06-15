from transitions import Machine


class Turnstile:
    pass


turnstile = Turnstile()
Machine(
    model=turnstile,
    states=["locked", "unlocked"],
    initial="locked",
    transitions=[
        {"trigger": "coin", "source": "locked", "dest": "unlocked"},
        {"trigger": "push", "source": "unlocked", "dest": "locked"},
    ],
)

turnstile.coin()

print(turnstile.state.lower())
