import pytest
import pandas as pd
from main import (
    load_data,
    basic_info,
    check_missing_values,
    feature_engineering,
    visualize_data,
)

# URL for testing
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def test_load_data():
    """Test loading of dataset."""
    data = load_data(url)
    assert isinstance(data, pd.DataFrame), "Data should be a DataFrame"
    assert not data.empty, "Data should not be empty"


def test_basic_info(capsys):
    """Test basic info function output."""
    data = load_data(url)
    basic_info(data)
    captured = capsys.readouterr()
    assert "First 5 rows of data:" in captured.out
    assert "Last 5 rows of data:" in captured.out
    assert "Columns in dataset:" in captured.out
    assert "Dataset shape:" in captured.out


def test_check_missing_values(capsys):
    """Test missing values check and basic statistics output."""
    data = load_data(url)
    check_missing_values(data)
    captured = capsys.readouterr()
    assert "Missing values:" in captured.out
    assert "Basic statistics:" in captured.out


def test_feature_engineering():
    """Test feature engineering function."""
    data = load_data(url)
    data = feature_engineering(data)
    assert "petal_area" in data.columns, "Petal area column should be added"
    assert "species_code" in data.columns, "Species code column should be added"
    assert (
        data["species_code"].isin([0, 1, 2]).all()
    ), "Species codes should be mapped correctly"


@pytest.mark.mpl_image_compare
def test_visualize_data():
    """Test that visualize_data function runs without errors."""
    data = load_data(url)
    data = feature_engineering(data)
    try:
        visualize_data(data)
        assert True
    except Exception as e:  # Catch all exceptions, with specific error capture
        assert False, f"Visualization failed with error: {e}"
