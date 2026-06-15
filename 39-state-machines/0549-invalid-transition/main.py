from transitions import Machine, MachineError


class Turnstile:
    pass


t = Turnstile()
Machine(
    model=t,
    states=['locked', 'unlocked'],
    initial='locked',
    transitions=[
        {'trigger': 'coin', 'source': 'locked', 'dest': 'unlocked'},
        {'trigger': 'push', 'source': 'unlocked', 'dest': 'locked'},
    ],
)

# 'push' has no transition from 'locked'; the FSM rejects it and
# state stays unchanged.
try:
    t.push()
except MachineError:
    pass

print(t.state.lower())
