from load_csv import load
import matplotlib.pyplot as plt

def convert_to_numeric(value):
    return float(value[:-1])

def main():
    try:
        """
        Preping the data set and selecting Germany, France and Years
        """
        data = load("population_total.csv")
        Germany = [row[1:] for row in data if row[0] == "Germany"]
        France = [row[1:] for row in data if row[0] == "France"]
        Germany = Germany[0][1:]
        France = France[0][1:]
        Years = data[0]
        Years = data[0][2:]
        Germany = [convert_to_numeric(value) for value in Germany]
        France = [convert_to_numeric(value) for value in France]
        """
        Just ploting the values against the data
        """
        plt.plot(Years, Germany,'r')
        plt.plot(Years, France,'b')
        plt.xlabel("Years")
        plt.ylabel("Population (M)")
        plt.xticks(Years[::50])
        plt.title("Population of France and Germany")
        plt.legend()
        plt.show()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except AssertionError as e:
        print(AssertionError.__name__ + ":" + str(e))


if __name__ == "__main__":
    exit(main())