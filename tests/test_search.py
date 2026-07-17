import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # Navigate to Google
    page.goto("https://google.com")
    
    # Verify the initial page title
    expect(page).to_have_title("Google")
    
    # Locate the search bar by its name attribute and type the query
    search_input = page.locator("textarea[name='q']")
    search_input.fill("playwright python")
    
    # Press Enter to execute the search
    search_input.press("Enter")
    
    # Wait for the network to be idle or wait for results to load
    page.wait_for_load_state("networkidle")
    
    # Verify the results page title contains the query text
    expect(page).to_have_title("playwright python - Google Search")
