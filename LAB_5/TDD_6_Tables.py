"""
Multiplikationstabellen
Vi behöver en funktion som kan ge oss multiplikationstabellen.
Parametern "n" talar om vilket tals tabell vi ska skapa.
Parametern "limit" talar om var vi ska sluta.
Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:
3*1 = 3
3*2 = 6
3*3 = 9
3*4 = 12
multiplication_table(3, 4) → [3, 6, 9, 12]
"""
#def multiplication_table(n, limit):
 #   return [n * i for i in range(1, limit + 1)]

def multiplication_table(n, limit):
    return [n * i for i in range(1, int(limit) + 1)]

#AC1 Test standard table
def test_multiplication_basic():
    # This will fail because the function currently returns None
    assert multiplication_table(3, 4) == [3, 6, 9, 12]

#AC2 Test Zero and Negative limit
def test_multiplication_zero_limit():
    assert multiplication_table(5, 0) == []
    assert multiplication_table(5, -2) == []

# AC3:Floating point support
def test_multiplication_floats():
    # 0.5 * 1, 0.5 * 2
    assert multiplication_table(0.5, 2) == [0.5, 1.0]

"""
Test results
PASSED LAB_5/TDD_6_Tables.py::test_multiplication_basic
PASSED LAB_5/TDD_6_Tables.py::test_multiplication_zero_limit
PASSED LAB_5/TDD_6_Tables.py::test_multiplication_floats
============================================================
"""