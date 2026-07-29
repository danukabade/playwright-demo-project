from playwright.sync_api import Playwright


def test_path_parameter(playwright: Playwright):

    request = playwright.request.new_context()

    user_id = 5

    response = request.get(
        f"https://dummyjson.com/users/{user_id}"
    )

    print("Status Code:", response.status)

    data = response.json()

    print(data)

    assert response.status == 200

    assert data["id"] == user_id

    assert data["firstName"] == "Emma"