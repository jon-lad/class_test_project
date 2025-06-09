import pytest
from lib.present import Present

"""Test that we can unwrap after wrapping the toy"""
def test_unwrap_after_wrapping():
    present = Present()
    present.wrap("toy")

    actual = present.unwrap()

    expected = "toy"

    assert actual == expected

"""Test unwrapping without wrapping raises an exception"""
def test_unwrapping_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()

    error_message = str(e.value)

    expected = "No contents have been wrapped."

    assert error_message == expected

"""Test wrapping twice raises an exception"""
def test_wrapping_two_different_things():
    present = Present()
    present.wrap("toy")
    with pytest.raises(Exception) as e:
        present.wrap("jewelry")

    error_message = str(e.value)

    expected = "A contents has already been wrapped."

    assert error_message == expected
