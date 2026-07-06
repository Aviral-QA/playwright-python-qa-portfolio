from pages.login_page import LoginPage


def test_login_page_visual(page, assert_snapshot):
    login_page = LoginPage(page)
    login_page.goto()
    page.wait_for_load_state("networkidle")

    assert_snapshot(page.screenshot(), "login_page.png")


def test_inventory_page_visual(page, assert_snapshot):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_load_state("networkidle")

    assert_snapshot(page.screenshot(), "inventory_page.png")