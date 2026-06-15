from transitions import Machine


class TrafficLight:
    pass


t = TrafficLight()
Machine(
    model=t,
    states=['red', 'green', 'yellow'],
    initial='red',
    transitions=[
        {'trigger': 'next', 'source': 'red', 'dest': 'green'},
        {'trigger': 'next', 'source': 'green', 'dest': 'yellow'},
        {'trigger': 'next', 'source': 'yellow', 'dest': 'red'},
    ],
)

t.next()  # red -> green
t.next()  # green -> yellow
print(t.state.lower())
