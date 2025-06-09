import pytest
from lib.password_checker import PasswordChecker

"""Test that the password checker check method returns true when the 
password is 8+ character"""
def test_check_returns_true_when_password_length_is_over_eight():
    password_checker = PasswordChecker()
    
    actual = password_checker.check("12345678")

    expected = True

    assert actual == expected

"""Test that error is thrown when shorter than 8 charcters"""
def test_check_returns_true_when_password_length_is_over_eight():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")

    error_message = str(e.value)

    expected = "Invalid password, must be 8+ characters."

    assert error_message == expected