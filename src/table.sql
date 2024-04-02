CREATE TABLE Type (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Task (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    level INT CHECK (level >= 0 AND level <= 3),
    time FLOAT,
    des VARCHAR(255),
    click BOOLEAN,
    type INTEGER CHECK (type = 0 OR type = 1),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE REPECT_Task(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
