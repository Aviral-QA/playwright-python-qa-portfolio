class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.inventory_items = page.locator(".inventory_item")

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()