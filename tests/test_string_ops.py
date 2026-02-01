from myproj import upper


def test_uppercase():
    assert upper("hello") == "HELLO"


def test_uppercase_mixed_case():
    assert upper("Hello World") == "HELLO WORLD"


def test_uppercase_empty_string():
    assert upper("") == ""
