from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_add_item_to_cart(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_complete_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    assert cart_page.get_item_count() == 1
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_order()

    assert "Thank you" in checkout_page.get_confirmation_text()