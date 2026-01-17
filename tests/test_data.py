import pytest
from src.data import DataHandling

class testDataHandling:

    def test_init():
        test = DataHandling(":memory:")
        data = test.get_all_data()

        for line in data:
            if line:
                assert True
            else:
                assert False