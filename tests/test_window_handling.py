from playwright.sync_api import Page, expect # type: ignore
def test_switch_window(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")
    rows = page.locator("#courses_table tbody tr")
    first_row = rows.nth(0)
    cells = first_row.locator("td")
    with page.expect_popup() as popup_info:
        cells.nth(5).locator('a').click()
    new_page = popup_info.value
    new_page.wait_for_load_state()
    print("Old URL :", page.url)
    print("New URL :", new_page.url)

    print("Old Title :", page.title())
    print("New Title :", new_page.title())

    assert "udemy.com" in new_page.url
    assert "Advanced Selenium testing framework with Java" in new_page.title()
    new_page.close()
    page.wait_for_timeout(3000)