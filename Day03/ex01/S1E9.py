from abc import ABC, abstractmethod


class Character(ABC):
    """ Class inherits from ABC """
    def __init__(self, first_name, is_alive=True):
        """ init inits data of the class """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ Abstract method of the class file """
        pass
    
class Stark(Character):
    """ Class that inherits from GOT Chars """
    def die(self):
        """ Abstract class implementation for Starks """
        self.is_alive = False
