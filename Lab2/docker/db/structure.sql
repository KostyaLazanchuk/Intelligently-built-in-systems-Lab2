CREATE TABLE processed_agent_data (
    id SERIAL PRIMARY KEY,
    road_state STRING NOT NULL,
    user_id INTEGER NOT NULL,
    x FLOAT,
    y FLOAT,
    z FLOAT,
    latitude FLOAT,
    longitude FLOAT,
    timestamp TIMESTAMP
);