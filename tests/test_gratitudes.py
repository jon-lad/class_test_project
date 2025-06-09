from lib.gratitudes import Gratitudes

""" Test that initialy gratitudes holds no gratitudes"""
def test_initially_gratitudes_is_empy():
    gratitudes = Gratitudes()

    actual = gratitudes.format()

    expected = "Be grateful for: "

    assert actual == expected

"""Test adding multiple gatitudes get returned in the correct format"""
def test_initially_gratitudes_is_empy():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    gratitudes.add("wealth")
    gratitudes.add("friends")

    actual = gratitudes.format()

    expected = "Be grateful for: health, wealth, friends"

    assert actual == expected