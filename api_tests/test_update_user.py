from playwright.sync_api import Playwright


def test_update_user(playwright: Playwright):

    request = playwright.request.new_context()

    payload = {
        "firstName": "Daneshwari",
        "lastName": "Kabade",
        "age": 25
    }

    response = request.put(
        "https://dummyjson.com/users/1",
        data=payload
    )

    print("Status Code:", response.status)

    data = response.json()

    print(data)

    assert response.status == 200
    assert data["id"] == 1
    assert data["firstName"] == "Daneshwari"
    assert data["lastName"] == "Kabade"
    assert data["age"] == 25