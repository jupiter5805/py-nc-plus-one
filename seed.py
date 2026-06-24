import json

from connection import connection


def seed():
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS rsvps;")
    cursor.execute("DROP TABLE IF EXISTS events;")
    cursor.execute("DROP TABLE IF EXISTS venues;")
    cursor.execute("DROP TABLE IF EXISTS users;")

    cursor.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    """)

    cursor.execute("""
        CREATE TABLE venues (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address TEXT,
            capacity INT
        );
    """)

    cursor.execute("""
        CREATE TABLE events (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            starts_at TIMESTAMPTZ NOT NULL,
            ends_at TIMESTAMPTZ NOT NULL,
            organiser_id INT REFERENCES users(id),
            venue_id INT REFERENCES venues(id),
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    """)

    cursor.execute("""
        CREATE TABLE rsvps (
            id SERIAL PRIMARY KEY,
            attendee_id INT REFERENCES users(id),
            event_id INT REFERENCES events(id),
            created_at TIMESTAMPTZ DEFAULT NOW()
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

    with open("db/data/events.json", "r") as file:
        events = json.load(file)

    for event in events:
        cursor.execute("""
            INSERT INTO events
            (title, description, starts_at, ends_at, organiser_id, venue_id)
            VALUES
            (%s, %s, %s, %s, %s, %s);
        """, [
            event["title"],
            event["description"],
            event["starts_at"],
            event["ends_at"],
            event["organiser_id"],
            event["venue_id"]
        ])

    with open("db/data/rsvps.json", "r") as file:
        rsvps = json.load(file)

    for rsvp in rsvps:
        cursor.execute("""
            INSERT INTO rsvps
            (attendee_id, event_id)
            VALUES
            (%s, %s);
        """, [rsvp["attendee_id"], rsvp["event_id"]])

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    seed()
