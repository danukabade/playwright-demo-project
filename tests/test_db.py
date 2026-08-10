from utils.db_connection import get_connection


def test_database_connection():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    print(rows)

    assert len(rows) > 0

    cursor.close()
    connection.close()