from playwright.sync_api import Playwright


def test_login(playwright: Playwright):

    request = playwright.request.new_context()

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = request.post(
        "https://dummyjson.com/auth/login",
        data=payload
    )

    print("Status Code:", response.status)

    data = response.json()

    print(data)

    assert response.status == 200

    assert "accessToken" in data

    assert data["username"] == "emilys"