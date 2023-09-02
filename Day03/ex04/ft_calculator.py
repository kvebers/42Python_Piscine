class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculator"""
        sum = 0
        for i in range(len(V1)):
            sum = sum + V1[i] * V2[i]
        print(sum)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """New Vector SUM VECTOR"""
        sum = []
        for i in range(len(V1)):
            sum.append(V1[i] + V2[i])
        print(sum)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """New Vector SUB VECTOR"""
        sum = []
        for i in range(len(V1)):
            sum.append(V1[i] - V2[i])
        print(sum)
