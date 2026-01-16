import pytest
from src.main import DataHandling

def test_init_of_DataHandling():
    try:
        test = DataHandling(":memory:") #that name makes the database temp for data
        assert True
    except Exception as e:
        assert False, e

def test_get_data_from_datbase():
    test = DataHandling(":memory:")
    data = test.get_all_data()