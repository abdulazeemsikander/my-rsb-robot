class StateMachine:
    def __init__(self):
        self.state = "INITIALIZATION"

    def transition_to(self, new_state):
        print(f"Transitioning from {self.state} to {new_state}")
        self.state = new_state
