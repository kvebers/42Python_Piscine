from S1E9 import Character


class Baratheon(Character):
    """ Class that inherits from GOT Chars """
    def __init__(self, first_name, is_alive=True):
        """INIT"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Abstract class implementation for Baratheons """
        self.is_alive = False

    def __str__(self):
        """RETURNS THE STRING REPRESENTATION OF SELF"""
        return f"<Baratheon: {self.first_name} of Vector \
            ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """Just repeat of __Str__()"""
        return self.__str__()


class Lannister(Character):
    """ Class that inherits from GOT Chars LANNISTER """
    def __init__(self, first_name, is_alive=True):
        """INIT"""
        Character.__init__(self, first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """ Abstract class implementation for Lannisters """
        self.is_alive = False

    def __str__(self):
        """RETURNS THE STRING REPRESENTATION OF SELF"""
        return f"<Lanister: {self.first_name} of Vector \
              ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        """Just repeat of __Str__()"""
        return self.__str__()

    def create_lannister(first_name, is_alive=True):
        """THE Lanister thingy"""
        return Lannister(first_name, is_alive)
