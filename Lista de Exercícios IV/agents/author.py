from agents.agent import Agent

class Author (Agent):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.books_published = []
    
    