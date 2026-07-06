class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_checkout_info(self, first, last, zip_code):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_text(self):
        return self.complete_header.text_content()