from playwright.sync_api import Playwright


def test_headers(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.get(
        "https://dummyjson.com/users",
        headers={
            "Accept": "application/json"
        }
    )

    print("Status Code:", response.status)

    data = response.json()

    print("Total Users:", data["total"])

    assert response.status == 200

    assert data["total"] > 0