"""
1a Find suitable test data for the following function, which converts degrees Celsius to degrees Fahrenheit.
def c_to_f(degree):
if degree < -273.15:
return None
return degree * 9 / 5 + 32
1b What equivalence classes does the parameter degree have?
1c Write a test case.
"""
import pytest

def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

@pytest.mark.parametrize("celsius, expected_fahrenheit", [
    (-300, None),                # Invalid class
    (-273.15, pytest.approx(-459.67)), # Boundary value (Absolute Zero)
    (0, 32.0),                   # Valid class (Freezing point)
    (100, 212.0),                # Valid class (Boiling point)
    (-40, -40.0),                # Valid class (The crossover point)
])

def test_c_to_f(celsius, expected_fahrenheit):
    assert c_to_f(celsius) == expected_fahrenheit

"""
test results:

LAB_5/TDD_1_Celsius.py::test_c_to_f[-300-None] PASSED                                                                                                                        [ 20%]
LAB_5/TDD_1_Celsius.py::test_c_to_f[-273.15-expected_fahrenheit1] PASSED                                                                                                     [ 40%]
LAB_5/TDD_1_Celsius.py::test_c_to_f[0-32.0] PASSED                                                                                                                           [ 60%]
LAB_5/TDD_1_Celsius.py::test_c_to_f[100-212.0] PASSED                                                                                                                        [ 80%]
LAB_5/TDD_1_Celsius.py::test_c_to_f[-40--40.0] PASSED                                                                                                                        [100%]

"""