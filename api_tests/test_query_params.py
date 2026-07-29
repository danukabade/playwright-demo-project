from playwright.sync_api import Playwright


def test_query_parameters(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.get(
        "https://dummyjson.com/users",
        params={
            "limit": 5,
            "skip": 10
        }
    )

    print("Status Code:", response.status)

    data = response.json()

    print(data)

    assert response.status == 200

    assert len(data["users"]) == 5

    assert data["limit"] == 5

    assert data["skip"] == 10

    assert data["total"] > 0