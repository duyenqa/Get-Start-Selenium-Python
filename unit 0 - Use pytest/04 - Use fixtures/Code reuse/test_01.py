import pytest

@pytest.fixture
def set_up():
    print("Launch browser")
    print("Log In")
    print("Home products")

def test_add_product(set_up):
    print("Add Item in cart")

def test_remove_product(set_up):
    print("Remove Item in cart")

def test_checkout(set_up):
    print("Checkout Items")

""" Result:
Launch browser
Log In
Home products
Add Item in cart

Launch browser
Log In
Home products
Remove Item in cart

Launch browser
Log In
Home products
Checkout Items
"""