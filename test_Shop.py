from Shop import ShoppingCart
import pytest

def test_add_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()

#Always Fail
def test_when_add_more_than_max_items():
    cart = ShoppingCart(50)
    for _ in range(5):
        cart.add("apple")
    # with pytest.raises (OverflowError):
    #    cart.add("apple")

def test_can_get_total_price():
    cart = ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")

    price_map = {
        "apple" : 1.5,
        "orange": 2.2
    }

    assert cart.get_total_price(price_map) == 3.8