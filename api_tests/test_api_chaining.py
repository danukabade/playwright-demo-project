from playwright.sync_api import Playwright


def test_api_chaining(playwright: Playwright):

    request = playwright.request.new_context()

    # Step 1: Login
    login_response = request.post(
        "https://dummyjson.com/auth/login",
        data={
            "username": "emilys",
            "password": "emilyspass"
        }
    )

    assert login_response.status == 200

    login_data = login_response.json()

    token = login_data["accessToken"]

    print("Access Token:", token)

    # Step 2: Use token in another request
    profile_response = request.get(
        "https://dummyjson.com/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    print("Profile Status:", profile_response.status)

    profile = profile_response.json()

    print(profile)

    assert profile_response.status == 200

    assert profile["username"] == "emilys"