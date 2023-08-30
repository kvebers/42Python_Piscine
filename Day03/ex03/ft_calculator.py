class calculator:
    """JUST LOOK UP"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [each + object for each in self.vector]
        print(self.vector)
        return self.vector
        """+"""
    def __mul__(self, object) -> None:
        self.vector = [each * object for each in self.vector]
        print(self.vector)
        return self.vector
        """*"""
    def __sub__(self, object) -> None:
        self.vector = [each - object for each in self.vector]
        print(self.vector)
        return self.vector
        """-"""
    def __truediv__(self, object) -> None:
        """/"""
        if (object == 0):
            return self.vector
        else:
            self.vector = [each / object for each in self.vector]
            print(self.vector)
            return self.vector