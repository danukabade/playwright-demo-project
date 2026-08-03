# from playwright.sync_api import expect

# def test_iframe(page):

#     page.goto("https://the-internet.herokuapp.com/iframe")

#     page.wait_for_timeout(2000)

#     frame = page.frame_locator("#mce_0_ifr")

#     editor = frame.locator("#tinymce")

#     editor.click()

#     editor.press("Meta+A")      # Select all (Mac)

#     editor.press("Backspace")   # Delete existing text

#     editor.type("Hello Daneshwari")

#     page.wait_for_timeout(5000)


def test_iframe(page):

    page.goto("https://vinothqaacademy.com/iframe/")

    page.wait_for_timeout(2000)

    frame = page.frame_locator("iframe[title='Web Table']")

    frame.locator("#nameInput").fill("Daneshwari")

    page.wait_for_timeout(5000)
    