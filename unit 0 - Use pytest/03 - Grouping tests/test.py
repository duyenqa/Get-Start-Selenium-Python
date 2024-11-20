import pytest

@pytest.mark.smoke
def test_greet():
    assert "Hello" + " " + "World!" == "Hello World!"

@pytest.mark.regression
def test_subtraction():
    assert 2 - 1 == 1

@pytest.mark.regression
def test_multiplication():
    assert 2 * 3 == 6

@pytest.mark.medium
def test_entry():
    assert 1 == 1
