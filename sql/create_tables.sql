-- Postgres DDL: owners, cars, sales

CREATE TABLE IF NOT EXISTS owners (
  owner_id SERIAL PRIMARY KEY,
  owner_name VARCHAR(200) NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  UNIQUE(phone)
);

CREATE TABLE IF NOT EXISTS cars (
  car_id SERIAL PRIMARY KEY,
  car_name VARCHAR(200) NOT NULL,
  model VARCHAR(100),
  base_price NUMERIC(12,2)
);

CREATE TABLE IF NOT EXISTS sales (
  sale_id SERIAL PRIMARY KEY,
  sale_date DATE NOT NULL,
  owner_phone VARCHAR(20), -- temporary until owner_id resolved in ETL
  owner_name VARCHAR(200),
  address TEXT,
  car_name VARCHAR(200),
  car_model VARCHAR(100),
  purchase_price NUMERIC(12,2),
  created_at TIMESTAMP DEFAULT now()
);

-- Index for date range queries
CREATE INDEX IF NOT EXISTS idx_sales_sale_date ON sales(sale_date);
