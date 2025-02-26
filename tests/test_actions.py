from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")

    expect
