import sqlite3

SCHEMA = '''
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS topics (
    id            INTEGER PRIMARY KEY,
    title         TEXT NOT NULL,
    notes         TEXT,
    learned_date  TEXT NOT NULL,
    span          INTEGER NOT NULL CHECK (span BETWEEN 1 AND 6),
    timestamp     TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS revisions (
    id                INTEGER PRIMARY KEY,
    topic_id          INTEGER NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    interval          INTEGER NOT NULL,
    org_due_date      TEXT NOT NULL,
    cur_due_date      TEXT NOT NULL,
    status            TEXT NOT NULL DEFAULT 'pending'
                      CHECK (status IN ('pending', 'completed')),
    completed_date    TEXT,
    recall_score      INTEGER CHECK (recall_score BETWEEN 1 AND 5),
    reschedule_count  INTEGER NOT NULL DEFAULT 0,
    google_event_id   TEXT
);

CREATE INDEX IF NOT EXISTS due_idx ON revisions(status, cur_due_date);
'''

def connect(path="revision.db"):
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.executescript(SCHEMA)
    return connection