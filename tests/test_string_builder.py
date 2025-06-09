from lib.string_builder import StringBuilder

"""
Add a string (hat) and see if the size method returns the correct value (3)
expected: 3
"""
def test_size_of_string_entered():
    string_builder = StringBuilder()
    string_builder.add("hat")

    actual = string_builder.size()

    expected = 3

    assert actual == expected

"""
Add a string ("hat") and see if the output method returns the 
correct string ("hat")
expected: "hat"
"""
def test_returns_string_entered():
    string_builder = StringBuilder()
    string_builder.add("hat")

    actual = string_builder.output()

    expected = "hat"

    assert actual == expected
"""
Add multiple strings "hat" and "cart"  to see if the size method returns 
the correct value (7)
expected: 7
"""
def test_size_of_strings_entered():
    string_builder = StringBuilder()
    string_builder.add("hat")
    string_builder.add("cart")

    actual = string_builder.size()

    expected = 7

    assert actual == expected

"""
Add multiple strings "hat" and "cart"  to see if the outpu method returns 
the correct string "hatcart"
expected: "hatcart"
"""
def test_returns_strings_entered():
    string_builder = StringBuilder()
    string_builder.add("hat")
    string_builder.add("cart")

    actual = string_builder.output()

    expected = "hatcart"

    assert actual == expected