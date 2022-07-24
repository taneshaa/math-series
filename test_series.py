from series import fibonacci, lucas, sum_series


def test_fibonacci_input_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_input_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_input_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_input_3():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_fibonacci_input_4():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected



def test_lucas_one():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_two():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_sum_series_0():
    actual = sum_series(1)
    expected = 2
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(2)
    expected = 2
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2)
    expected = 2
    assert actual == expected