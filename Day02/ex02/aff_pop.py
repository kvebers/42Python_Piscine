from load_csv import load
import matplotlib.pyplot as plt


def isCountry(row, countrColumn, targerCountry):
    """Specify the Country here"""
    return row[countrColumn] == targerCountry


def convertToMils(value):
    if (value[-1] == "M"):
        return float(value[:-1])
    elif (value[-1] == "k"):
        value = float(value[:-1])
        return value / 1000
    else:
        value = float(value[:-1])
        return value / 1000000


def main():
    try:
        """
        Preping the data set and selecting Germany, France and Years
        """
        data = load("population_total.csv")
        Germany = data[data.apply(isCountry, axis=1, args=(0, "Germany"))]
        France = data[data.apply(isCountry, axis=1, args=(0, "France"))]
        Latvia = data[data.apply(isCountry, axis=1, args=(0, "Latvia"))]
        HolySee = data[data.apply(isCountry, axis=1, args=(0, "Holy See"))]
        Years = data.columns[2:]
        Germany = Germany.iloc[0, 2:].apply(convertToMils)
        France = France.iloc[0, 2:].apply(convertToMils)
        Latvia = Latvia.iloc[0, 2:].apply(convertToMils)
        HolySee = HolySee.iloc[0, 2:].apply(convertToMils)
        # print(HolySee)
        # print(Latvia)
        # Plot population data
        plt.plot(Years, Germany, 'r', label="Germany")
        plt.plot(Years, France, 'b', label="France")
        plt.plot(Years, Latvia, 'g', label="Latvia")
        plt.plot(Years, HolySee, 'black', label="Holy See")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.xticks(Years[::50])
        plt.yticks((20, 40, 60, 80, 100))
        plt.title("Population of France, Germany, Holy See and Latvia")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()