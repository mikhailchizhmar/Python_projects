SQL preprocessing before running reporting_client_v3.py:
```sql
CREATE DATABASE spaceship_reports;
CREATE USER newtonbe WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE spaceship_reports TO newtonbe;
GRANT postgres TO newtonbe;

CREATE TABLE spaceships (
    id SERIAL PRIMARY KEY,
    alignment VARCHAR,
    name VARCHAR,
    class_ VARCHAR,
    length INTEGER,
    crew_size INTEGER,
    armed BOOLEAN
);

CREATE TABLE officers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    rank VARCHAR
);

CREATE TABLE spaceship_officers (
    id SERIAL PRIMARY KEY,
    spaceship_id INTEGER REFERENCES spaceships(id),
    officer_id INTEGER REFERENCES officers(id)
);
```