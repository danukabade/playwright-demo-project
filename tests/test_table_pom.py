from pages.table_page import TablePage


def test_python_filter(page):

    table = TablePage(page)

    table.open()

    table.select_language("Python")

    assert table.row_count() > 0
    table.page.wait_for_timeout(3000)