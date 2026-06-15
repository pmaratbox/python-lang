from transitions import Machine


class Workflow:
    pass


workflow = Workflow()
Machine(
    model=workflow,
    states=["idle", "pending", "approved"],
    initial="idle",
    transitions=[
        {"trigger": "submit", "source": "idle", "dest": "pending"},
        {"trigger": "approve", "source": "pending", "dest": "approved"},
    ],
)

workflow.submit()
workflow.approve()

print(workflow.state.lower())
