from playwright.sync_api import Playwright, APIRequestContext
def test_get_users(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get("https://dummyjson.com/users")

    print("Status Code:", response.status)

    data = response.json()
    assert response.status == 200

    print("Total Users:", data["total"])

    print(data["users"][0])

    print("First Name:", data["users"][0]["firstName"])

    assert data["users"][0]["firstName"] == "Emily"

    print(data)
