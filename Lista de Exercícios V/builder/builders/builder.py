from abc import ABC, abstractmethod

class Builder:

    @abstractmethod
    def reset(self):
        pass
        
    @abstractmethod
    def prepare_cake_type(self, type):
        pass

    @abstractmethod
    def prepare_cake_style(self, style):
        pass