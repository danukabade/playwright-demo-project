import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # Navigate to Google
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    # Verify the initial page title
    expect(page).to_have_title("Test Login | Practice Test Automation")
    
    page.wait_for_timeout(10000)
    # # Locate the search bar by its name attribute and type the query
    userid_input = page.locator("#username")
    userid_input.fill("student")

    passwd_input = page.locator("#password")
    passwd_input.fill("Password123")

    submit_btn = page.locator("#submit")
    submit_btn.press()

    # Pause the test for 3 seconds (3000 milliseconds)
    page.wait_for_timeout(10000)

    
    
    # Wait for the network to be idle or wait for results to load
    page.wait_for_load_state("networkidle")
    
    # Verify the results page title contains the query text
    # expect(page).to_have_title("playwright python - Google Search")
