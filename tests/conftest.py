## Fixtures
# import pytest
# from pages.table_page import TablePage


# @pytest.fixture
# def table(page):
#     return TablePage(page)

## Hooks 
import pytest
from pages.table_page import TablePage


@pytest.fixture
def table(page):

    print("Before Test")

    table = TablePage(page)

    yield table

    print("After Test")