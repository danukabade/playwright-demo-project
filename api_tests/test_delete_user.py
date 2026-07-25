from playwright.sync_api import Playwright


def test_delete_user(playwright: Playwright):

    request = playwright.request.new_context()

    response = request.delete(
        "https://dummyjson.com/users/1"
    )

    print("Status Code:", response.status)

    data = response.json()

    print(data)

    assert response.status == 200
    assert data["id"] == 1
    assert data["isDeleted"] == True
    assert data["deletedOn"] is not None