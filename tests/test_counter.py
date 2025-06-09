from lib.counter import Counter

"""
Test Counter with initial number (3)
expect: report method to return "Counted to 3 so far."
"""
def test_counter_with_initial_number():
    counter = Counter()
    counter.add(3)

    actual = counter.report()

    expected = "Counted to 3 so far."

    assert actual == expected

"""
Test Counter with initial number (3) and another number (5)
expect: report method to return "Counted to 8 so far."
"""
def test_counter_with_additional_number():
    counter = Counter()
    counter.add(3)
    counter.add(5)

    actual = counter.report()

    expected = "Counted to 8 so far."

    assert actual == expected
