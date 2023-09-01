from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter 

def main():
    try:
        """
        Preping the data set and selecting Germany, France and Years
        """
        data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life = load("life_expectancy_years.csv")
        count = [row[0] for row in data[1:]]
        index = data[0].index("1900")
        countIncome = [row[index] for row in data[1:]]
        life_index = life[0].index("1900")
        lifeExp = [(row[life_index]) for row in life[1:]]
        plt.scatter(countIncome, lifeExp)
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy (Years)")
        plt.title("1900")
        plt.xticks([x * 1e4 for x in range(0, 1000, 2000)])
        plt.yticks([y for y in range(10, 101, 10)])
        for i, country in enumerate(count):
            if i % 20 == 0 or country == "Latvia":
                plt.annotate(country, (countIncome[i], lifeExp[i]))
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())