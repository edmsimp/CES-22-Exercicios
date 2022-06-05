# Main class to describe agents, the other ones in this folder are children
# classes for each agent type.
class Agent:
    def __init__ (self, name, email):
        self.name = name
        self.email = email