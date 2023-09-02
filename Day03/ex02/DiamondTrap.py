from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Specificly forcing it to inherit from
        Baratheon Can Change to Lanister for testing purposes"""
        super().__init__(first_name, is_alive)
        # Baratheon.__init__(self, first_name, is_alive)
        # Lannister.__init__(self, first_name, is_alive)

    def set_eyes(self, color):
        """setter for eye color"""
        self.eyes = color

    def set_hairs(self, color):
        """setter for hair color"""
        self.hairs = color

    def get_eyes(self):
        """getter for eye color"""
        return self.eyes

    def get_hairs(self):
        """getter for hair"""
        return self.hairs
