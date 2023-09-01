from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Preping the data set and selecting Germany, France and Years"""
    try:
        data = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life = load("life_expectancy_years.csv")
        countIncome = data[['country'] + ["1900"]]
        lifeExp = life[['country'] + ["1900"]]
        MergedData = pd.merge(countIncome, lifeExp, on='country', how='inner')
        MergedData.columns = ['Country', 'Gross Domestic Product',
                              'Life Expectancy (Years)']
        plt.scatter(MergedData['Gross Domestic Product'],
                    MergedData['Life Expectancy (Years)'])
        plt.xlabel("Gross Domestic Product ($ I guess IDK)")
        plt.ylabel("Life Expectancy (Years)")
        plt.title("1900")
        plt.yticks((20, 25, 30, 35, 40, 45, 50, 55))
        plt.xscale('log')
        customTicks = [300, 1000, 10000]
        customLabels = ['300', '1k', '10k']
        plt.xticks(customTicks, customLabels)
        plt.legend()
        plt.show()
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    exit(main())
