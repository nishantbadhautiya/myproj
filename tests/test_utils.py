from myproj import greet


def test_greet_name():
    assert greet("Nishant") == "Hello, Nishant!"


def test_greet_empty_name():
    assert greet("") == "Hello, !"
