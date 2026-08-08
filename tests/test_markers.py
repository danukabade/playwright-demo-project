import pytest


@pytest.mark.smoke
def test_login():
    print("Login test")


@pytest.mark.sanity
def test_search():
    print("Search test")


@pytest.mark.regression
def test_payment():
    print("Payment test")