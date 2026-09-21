from utils.db_connection import get_connection


def test_insert_and_verify_user():

    connection = get_connection()
    cursor = connection.cursor()

    # Insert data
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        ("Test User", "testuser@example.com")
    )

    connection.commit()

    # Read the inserted data
    cursor.execute(
        "SELECT name, email FROM users WHERE email = %s",
        ("testuser@example.com",)
    )

    user = cursor.fetchone()

    print(user)

    # Validate database data
    assert user is not None
    assert user[0] == "Test User"
    assert user[1] == "testuser@example.com"

    cursor.close()
    connection.close()