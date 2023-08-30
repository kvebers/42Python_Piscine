from load_csv import load
from ft_filter import ft_filter
import matplotlib.pyplot as plt


def is_Germany(row):
    return row[0] == "Germany"

def main():
    try:
        """
        Preping the data set and selecting Germany and Years
        """
        data = load("life_expectancy_years.csv")
        Germany = ft_filter(is_Germany, data)
        Germany = Germany[0][1:]
        Years = data[0]
        Years = Years[1:]
        """
        Just ploting the values against the data
        """
        plt.plot(Years, Germany,'r')
        plt.xlabel("Years")
        plt.ylabel("Life Expectancy")
        plt.xticks(Years[::50])
        plt.yticks(Germany[::50])
        plt.title("Life Expectancy in Germany Over the Years")
        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))


if __name__ == "__main__":
    exit(main())