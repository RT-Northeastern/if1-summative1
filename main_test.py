# imports our function rt_fizznumber from rt_fizzbuzz file
from rt_fizzbuzz import rt_fizznumber

# defines our function and validates if fizz_number is divisable by 2
def test_fizz(): 
    assert rt_fizznumber(4) == "Fizz"
    assert rt_fizznumber (5) != "Fizz"
    assert rt_fizznumber (2) == "Fizz"

# defines our function and validates if fizz_number is divisable by 3
def test_buzz(): 
    assert rt_fizznumber(9) == "Buzz"
    assert rt_fizznumber(8) != "Buzz"
    assert rt_fizznumber(3) == "Buzz"

# defines our function and validates if fizz_number is divisable by 6
def test_fizzbuzz(): 
    assert rt_fizznumber(12) == "Fizzbuzz"
    assert rt_fizznumber (13) != "Fizzbuzz"
    assert rt_fizznumber(6) == "Fizzbuzz"
