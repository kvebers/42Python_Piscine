class calculator:
    """JUST LOOK UP"""
    def __init__(self, vector):
        """INIT"""
        self.vector = vector

    def __add__(self, object) -> None:
        """+"""
        self.vector = [each + object for each in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """*"""
        self.vector = [each * object for each in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """-"""
        self.vector = [each - object for each in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """/"""
        try:
            if (object == 0):
                raise ZeroDivisionError("Zero division not allowed")
            else:
                self.vector = [each / object for each in self.vector]
                print(self.vector)
                return self.vector
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
