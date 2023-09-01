class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        sum = 0
        if (len(V1) != len(V2)):
            print("Error")
            return
        for i in range(len(V1)):
            sum = sum + V1[i] * V2[i]
        print(sum)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        sum = []
        if (len(V1) != len(V2)):
            print("Error")
            return
        for i in range(len(V1)):
            sum.append(V1[i] + V2[i])
        print(sum)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sum = []
        if (len(V1) != len(V2)):
            print("Error")
            return
        for i in range(len(V1)):
            sum.append(V1[i] - V2[i])
        print(sum)
