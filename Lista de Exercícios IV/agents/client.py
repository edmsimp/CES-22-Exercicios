from agents.agent import Agent

class Client (Agent):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.past_orders = {}#"Title": "Quantity"}
    