from load_csv import load
import matplotlib.pyplot as plt


def isCountry(row, countrColumn, targerCountry):
    """Specify the Country here"""
    return row[countrColumn] == targerCountry


def main():
    """Displays the information about the countries"""
    try:
        data = load("life_expectancy_years.csv")
        # France = data[data.apply(isCountry, axis=1, args=(0, "France"))]
        # print(France)
        # France = France.iloc[:, 1:]
        Germany = data[data.apply(isCountry, axis=1, args=(0, "Germany"))]
        # print(Germany)
        Germany = Germany.iloc[:, 1:]
        Latvia = data[data.apply(isCountry, axis=1, args=(0, "Latvia"))]
        # print(Latvia)
        Latvia = Latvia.iloc[:, 1:]
        Years = data.columns[1:]
        plt.plot(Years, Germany.iloc[0], 'r', label="Germany")
        plt.plot(Years, Latvia.iloc[0], 'b', label="Latvia")
        # plt.plot(Years, France.iloc[0], 'g', label="France")
        plt.xlabel("Years")
        plt.ylabel("Life Expectancy")
        plt.xticks(Years[::50])
        plt.yticks(range(30, 101, 10))
        plt.title("Life Expectancy Over the Years")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
