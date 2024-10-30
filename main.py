# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(url):
    """Load the Iris dataset from a specified URL."""
    return pd.read_csv(url)


def basic_info(data):
    """Display basic dataset information."""
    print("First 5 rows of data:\n", data.head())
    print("\nLast 5 rows of data:\n", data.tail())
    print("\nColumns in dataset:\n", data.columns)
    print("\nDataset shape:", data.shape)


def check_missing_values(data):
    """Check for missing values and display basic statistics."""
    print("\nMissing values:\n", data.isnull().sum())
    print("\nBasic statistics:\n", data.describe())


def feature_engineering(data):
    """Add a petal area column and map species to numerical values."""
    data["petal_area"] = data["petal_length"] * data["petal_width"]
    species_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
    data["species_code"] = data["species"].map(species_mapping)
    return data


def visualize_data(data):
    """Generate plots to visualize the dataset."""
    sns.pairplot(
        data[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]],
        hue="species",
        palette="viridis",
    )
    plt.suptitle("Pairplot of Sepal and Petal Dimensions by Species", y=1.02)
    plt.show()

    sns.barplot(x="species", y="petal_area", data=data)
    plt.title("Average Petal Area by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Area")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.violinplot(
        x="species",
        y="sepal_length",
        hue="species",
        data=data,
        palette="viridis",
        dodge=False,
        legend=False,
    )
    plt.title("Distribution of Sepal Length by Species")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.violinplot(
        x="species",
        y="petal_length",
        hue="species",
        data=data,
        palette="magma",
        dodge=False,
        legend=False,
    )
    plt.title("Distribution of Petal Length by Species")
    plt.show()


if __name__ == "__main__":
    # URL for the Iris dataset
    iris_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

    # Load and process data
    iris_data = load_data(iris_url)
    basic_info(iris_data)
    check_missing_values(iris_data)
    iris_data = feature_engineering(iris_data)
    visualize_data(iris_data)
