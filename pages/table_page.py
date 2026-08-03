class TablePage:

    def __init__(self, page):
        self.page = page

        # self.java_radio = page.locator("#Java")
        # self.python_radio = page.locator("#Python")

        # self.beginner_checkbox = page.locator("#Beginner")
        # self.intermediate_checkbox = page.locator("#Intermediate")
        # self.advanced_checkbox = page.locator("#Advanced")

        self.enrollment_dropdown = page.locator("#enrollDropdown")
        self.sort_dropdown = page.locator("#sortBy")

        self.reset_button = page.locator("#resetFilters")

        self.rows = page.locator("#courses_table tbody tr")

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-table/")

    # def select_python(self):
    #     self.python_radio.click()

    # def select_java(self):
    #     self.java_radio.click()
    ## Instead of these above methods , for reusable , we use this ->
    def select_language(self, language):
       self.page.locator(f"input[value='{language}']").check()

    def select_level(self, level):
       self.page.locator(f"input[value='{level}']").check()

    def click_reset(self):
        self.reset_button.click()

    def select_min_enrollment(self, value):

      self.enrollment_dropdown.click()

      self.page.get_by_text(value).click()

    def sort_by(self, value):
        self.sort_dropdown.select_option(value)
    def row_count(self):
       return self.rows.count()