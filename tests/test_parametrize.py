# import pytest

# @pytest.mark.parametrize("username", ["Admin", "User", "Guest"])
# def test_login(username):
#     print("Testing:", username)



import pytest


@pytest.mark.parametrize("language", ["Python", "Java"])
def test_language_filter(table, language):

    table.open()

    table.select_language(language)

    assert table.row_count() > 0