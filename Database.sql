CREATE TABLE employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT,         
    role TEXT NOT NULL CHECK (role IN ('employee', 'manager'))     
);
INSERT INTO employees (employee_id, name, password, role)
VALUES ('125', 'Tanisha Bajaj', 'Tanisha123', 'manager');

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    employee_id VARCHAR(10),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);