from app.core import classify

def test_returns_number_as_string():
    assert classify(1) == "1"

def test_multiple_of_three_returns_fizz():
    assert classify(3) == "fizz"

def test_multiple_of_five_returns_buzz():
    assert classify(5) == "buzz"

def test_multiple_of_three_and_five_returns_fizzbuzz():
    assert classify(15) == "fizzbuzz"
