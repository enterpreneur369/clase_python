"""Configuration test file"""

import pytest
from clase_python.model.car import Car

@pytest.fixture()
def car():
    return Car('BMW', 2004, 4)

@pytest.fixture()
def carInvalid():
    return Car('MAZDA', 2004, 4)