CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    abn VARCHAR,
    entity_name TEXT,
    entity_type TEXT,
    status TEXT,
    address TEXT,
    postcode TEXT,
    state TEXT,
    start_date DATE,
    website TEXT,
    industry TEXT
);
