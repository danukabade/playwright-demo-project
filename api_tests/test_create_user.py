from playwright.sync_api import Playwright
def test_create_user(playwright: Playwright):
    request = playwright.request.new_context()
    payload = {
        "firstName": "Daneshwari",
        "lastName": "Kabade",
        "age": 24
    }
    response = request.post(
        "https://dummyjson.com/users/add",
        data = payload
    )
    print("Status Code:", response.status)
    data = response.json()

    print(data)
    assert response.status == 201
    assert data["firstName"] == "Daneshwari"
    assert data["lastName"] == "Kabade"
    assert data["age"] == 24