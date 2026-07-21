from playwright.sync_api import Page, expect

def test_open_table(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")

    expect(page).to_have_title("Test Table | Practice Test Automation")

    table = page.locator("#courses_table")

    expect(table).to_be_visible()

    rows = page.locator("#courses_table tbody tr")

    print("Total Rows:", rows.count())

    headers = page.locator("#courses_table thead tr th")

    print("Total Columns:", headers.count())
    #--read first row
    first_row = rows.nth(0)

    cells = first_row.locator("td")

    print("ID:", cells.nth(0).text_content())
    print("Course:", cells.nth(1).text_content())
    print("Language:", cells.nth(2).text_content())
    print("Level:", cells.nth(3).text_content())
    print("Enrollment:", cells.nth(4).text_content())
    print("Link:", cells.nth(5).text_content())
    
    #--Read all rows
    
    for i in range(rows.count()):

        # Get current row
        row = rows.nth(i)

        # Get all cells in that row
        cells = row.locator("td")

        assert cells.count() == 6

        print(f"\n========== Row {i + 1} ==========")

        print("ID:", cells.nth(0).text_content())
        print("Course:", cells.nth(1).text_content())
        print("Language:", cells.nth(2).text_content())
        print("Level:", cells.nth(3).text_content())
        print("Enrollment:", cells.nth(4).text_content())
        print("Link:", cells.nth(5).text_content())
   


def test_rest_assured_course(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    rows = page.locator("#courses_table tbody tr")

    found = False

    for i in range(rows.count()):

        row = rows.nth(i)

        cells = row.locator("td")

        course = cells.nth(1).text_content()

        if course == "REST Assured":

            found = True

            language = cells.nth(2).text_content()

            assert language == "Java"

            print("Course Found:", course)
            print("Language:", language)

            with page.expect_popup() as popup_info:
              cells.nth(5).locator("a").click()

            new_page = popup_info.value

            new_page.wait_for_load_state()

            # print("Old Page URL :", page.url)
            # print("New Page URL :", new_page.url)
            # print("New Page Title :", new_page.title())

            assert "rest-assured-for-beginners" in new_page.url

            assert "REST Assured" in new_page.title()

            new_page.close()

            break

    assert found, "REST Assured course was not found in the table."
    page.wait_for_timeout(3000)

# Language filter
def test_language_filter_java(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    page.get_by_role("radio", name="Java").check()


#through loop 
def test_language_filter_java(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")
    page.get_by_role("radio", name="Java").check()
    page.wait_for_timeout(1000)
    rows = page.locator("#courses_table tbody tr")
    for i in range(rows.count()):
        row = rows.nth(i)
        cells = row.locator("td")
        course = cells.nth(1).text_content()
        course = cells.nth(1).text_content()
        language = cells.nth(2).text_content()

        print(f"Row {i+1}")
        print("Course   :", course)
        print("Language :", language)
        print("----------------")
    page.wait_for_timeout(5000)
    
def test_level_filter_beginner(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")
    page.get_by_role("checkbox", name="Intermediate").uncheck()
    page.get_by_role("checkbox", name="Advanced").uncheck()
    page.wait_for_timeout(5000)

    rows = page.locator("#courses_table tbody tr")

    visible_count = 0

    for i in range(rows.count()):
        row = rows.nth(i)
        if not row.is_visible():
            continue

        visible_count += 1
        cells = row.locator("td")

        course = cells.nth(1).text_content()
        level = cells.nth(3).text_content()

        print(f"Row {i+1}")
        print("Course :", course)
        print("Level  :", level)
        print("----------------")

        assert level == "Beginner"
    print("Visible Rows:", visible_count)

    assert visible_count > 0

def test_min_enrollment_10000(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    page.get_by_role("button", name="Any").click()
    page.get_by_role("option", name="10,000+").click()

    rows = page.locator("#courses_table tbody tr")

    visible_count = 0

    for i in range(rows.count()):

        row = rows.nth(i)

        if not row.is_visible():
            continue

        visible_count += 1

        cells = row.locator("td")

        course = cells.nth(1).text_content()

        enrollment = cells.nth(4).text_content()

        enrollment = enrollment.replace(",", "")
        enrollment = int(enrollment)

        print(f"Row {visible_count}")
        print("Course      :", course)
        print("Enrollment  :", enrollment)
        print("----------------------")

        assert enrollment >= 10000

    print("Visible Rows:", visible_count)

    page.wait_for_timeout(5000)

def test_combined_filters(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")
    page.get_by_role("radio", name="Python").check()
    page.get_by_role("checkbox", name="Intermediate").uncheck()

    page.get_by_role("checkbox", name="Advanced").uncheck()

    page.get_by_role("button", name="Any").click()

    page.get_by_role("option", name="10,000+").click()
    rows = page.locator("#courses_table tbody tr")
    visible_count = 0

    for i in range(rows.count()):

        row = rows.nth(i)

        if not row.is_visible():
            continue

        visible_count += 1
        cells = row.locator("td")
        course = cells.nth(1).text_content()

        language = cells.nth(2).text_content()

        level = cells.nth(3).text_content()

        enrollment = cells.nth(4).text_content()
        enrollment = int(enrollment.replace(",", ""))
        print(f"\nRow {visible_count}")
        print("Course      :", course)
        print("Language    :", language)
        print("Level       :", level)
        print("Enrollments :", enrollment)
        assert language == "Python"
        assert level == "Beginner"
        assert enrollment >= 10000
    print(f"\nVisible Rows : {visible_count}")

    assert visible_count > 0

    page.wait_for_timeout(5000)

def test_no_results(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    # Java
    page.get_by_role("radio", name="Java").check()

    # Advanced only
    page.get_by_role("checkbox", name="Beginner").uncheck()
    page.get_by_role("checkbox", name="Intermediate").uncheck()

    # 10,000+
    page.get_by_role("button", name="Any").click()
    page.get_by_role("option", name="10,000+").click()

    message = page.locator("#noData")

    print(message.text_content())

    assert message.is_visible()
    assert message.text_content().strip() == "No matching courses."

    page.wait_for_timeout(5000)



def test_reset_button(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")

    # Change some filters
    page.get_by_role("radio", name="Java").check()
    page.get_by_role("checkbox", name="Intermediate").uncheck()
    page.get_by_role("checkbox", name="Advanced").uncheck()
    page.get_by_role("button", name="Any").click()
    page.get_by_role("option", name="10,000+").click()

    # Reset button should appear
    reset_button = page.locator("#resetFilters")
    assert reset_button.is_visible()

    print("Reset button is visible")

    # Click Reset
    reset_button.click()

    # Verify default filters
    assert page.get_by_role("radio", name="Any").is_checked()
    assert page.get_by_role("checkbox", name="Beginner").is_checked()
    assert page.get_by_role("checkbox", name="Intermediate").is_checked()
    assert page.get_by_role("checkbox", name="Advanced").is_checked()
    assert page.locator("#enrollDropdown").inner_text().strip() == "Any"

    print("All filters reset successfully")

    # Reset button should disappear
    assert not reset_button.is_visible()

    print("Reset button hidden")

    # Verify all rows are visible again
    rows = page.locator("#courses_table tbody tr")

    visible_count = 0

    for i in range(rows.count()):
        if rows.nth(i).is_visible():
            visible_count += 1

    print("Visible Rows:", visible_count)

    assert visible_count == rows.count()

    page.wait_for_timeout(3000)

def test_sort_by_enrollments(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    # Select Sort By -> Enrollments
    page.locator("#sortBy").select_option(label="Enrollments")

    rows = page.locator("#courses_table tbody tr")

    enrollments = []

    for i in range(rows.count()):

        row = rows.nth(i)

        if not row.is_visible():
            continue

        cells = row.locator("td")

        enrollment = cells.nth(4).text_content().strip()

        print("Enrollment:", enrollment)

        enrollment = enrollment.replace(",", "")

        enrollment = int(enrollment)

        enrollments.append(enrollment)

    print("Enrollment List:", enrollments)

    assert enrollments == sorted(enrollments)

    page.wait_for_timeout(3000)


def test_sort_by_course_name(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-table/")

    # Sort by Course Name
    page.locator("#sortBy").select_option(label="Course Name")

    rows = page.locator("#courses_table tbody tr")

    course_names = []

    for i in range(rows.count()):

        row = rows.nth(i)

        if not row.is_visible():
            continue

        cells = row.locator("td")

        course = cells.nth(1).text_content().strip()

        print(f"Row {i+1}: {course}")

        course_names.append(course)

    print("Course List:", course_names)

    assert course_names == sorted(course_names, key=str.lower)

    page.wait_for_timeout(3000)