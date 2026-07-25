from playwright.sync_api import Playwright
def test_patch_user(playwright: Playwright):
    request = playwright.request.new_context()
    payload = {
        "age": 26
    }
    response = request.patch(
        "https://dummyjson.com/users/1",
        data = payload
    )
    print("Status code:", response.status)
    data = response.json()
    print(data)
    assert response.status == 200
    assert data["age"] == 26