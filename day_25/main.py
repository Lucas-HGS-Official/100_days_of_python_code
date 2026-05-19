import csv

# from learning_python_env/lib64/python3.12/site-packages/pandas import pandas
import pandas


def main():
    if __name__ == "__main__":
        df = pandas.read_csv("weather_data.csv")
        print(df.to_string())
        with open("weather_data.csv", mode="r") as data_file:
            data = csv.reader(data_file)
            temperatures = []
            for row in data:
                if row[1] != "temp":
                    temperatures.append(int(row[1]))
        print(temperatures)


main()
