CREATE TABLE IF NOT EXISTS book (
    id SERIAL PRIMARY KEY,
    category text,
    title text,
    price numeric,
    stock text,
    rating text   
);
