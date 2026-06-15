from transitions import Machine


class Toggle:
    pass


toggle = Toggle()
Machine(
    model=toggle,
    states=['off', 'on'],
    initial='off',
    transitions=[
        {'trigger': 'toggle', 'source': 'off', 'dest': 'on'},
        {'trigger': 'toggle', 'source': 'on', 'dest': 'off'},
    ],
)

toggle.toggle()  # off -> on
toggle.toggle()  # on -> off
toggle.toggle()  # off -> on

print(toggle.state.lower())
