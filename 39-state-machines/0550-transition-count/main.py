from transitions import Machine


class Turnstile:
    def __init__(self):
        self.transition_count = 0

    def count_transition(self):
        # Runs after every state change, regardless of which event fired.
        self.transition_count += 1


t = Turnstile()
Machine(
    model=t,
    states=['locked', 'unlocked'],
    initial='locked',
    transitions=[
        {'trigger': 'coin', 'source': 'locked', 'dest': 'unlocked'},
        {'trigger': 'push', 'source': 'unlocked', 'dest': 'locked'},
    ],
    after_state_change='count_transition',
)

# Fire 3 valid events; the after-callback bumps the counter each time.
t.coin()   # locked   -> unlocked
t.push()   # unlocked -> locked
t.coin()   # locked   -> unlocked

print(t.transition_count)
