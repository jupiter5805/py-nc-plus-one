import json

from connection import connection


def seed():
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")

    cursor.execute("""
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            password VARCHAR NOT NULL
        );
    """)

    with open("db/data/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        cursor.execute("""
            INSERT INTO users
            (name, email, password)
            VALUES
            (%s, %s, %s);
        """, [user["name"], user["email"], user["password"]])

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    seed()
