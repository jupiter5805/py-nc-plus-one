# NC Plus One

NC Plus One is a Python and PostgreSQL portfolio project.

The project focuses on creating a local PostgreSQL database, connecting to it from Python, and building a seed function that can reset and repopulate the database with test data.

## Technologies

- Python
- PostgreSQL
- SQL
- python-dotenv
- pytest

## Database Setup

To create the local database, run:

```bash
psql -f db/setup.sql
```

This will drop and recreate the `nc_plus_one` database.

## Environment Variables

Create a `.env` file in the root of the project.

Add the following:

```env
PGDATABASE=nc_plus_one
```

A `.env.example` file is included to show which environment variables are needed.