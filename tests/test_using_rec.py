import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")
    page.get_by_role("link", name="Log out").click()
    expect(page.locator("h2")).to_contain_text("Test login")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
