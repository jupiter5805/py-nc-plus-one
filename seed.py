import json

from connection import connection


def seed():
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS venues;")

    cursor.execute("""
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            password VARCHAR NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE venues (
            venue_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            address VARCHAR,
            capacity INT NOT NULL
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

    with open("db/data/venues.json", "r") as file:
        venues = json.load(file)

    for venue in venues:
        cursor.execute("""
            INSERT INTO venues
            (name, address, capacity)
            VALUES
            (%s, %s, %s);
        """, [venue["name"], venue["address"], venue["capacity"]])

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    seed()
