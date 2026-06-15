from transitions import Machine


class Door:
    pass


door = Door()
Machine(
    model=door,
    states=['locked', 'unlocked', 'open'],
    initial='locked',
    transitions=[
        {'trigger': 'unlock', 'source': 'locked', 'dest': 'unlocked'},
        # 'open' is only valid from 'unlocked' (guarded by its source state)
        {'trigger': 'open', 'source': 'unlocked', 'dest': 'open'},
    ],
)

door.unlock()
door.open()
print(door.state.lower())
