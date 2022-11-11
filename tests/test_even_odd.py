from sse_numbers import isEven, isOdd

def test_even_odd():
    assert isEven(2)
    assert not isEven(3)
    assert isOdd(3)
    assert not isOdd(4)

