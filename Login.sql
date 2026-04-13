CREATE TABLE employees (
    employee_id VARCHAR(10) PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT,         
    role TEXT NOT NULL CHECK (role IN ('employee', 'manager'))     
);

INSERT INTO employees (employee_id, name, password, role)
VALUES ('125', 'Tanisha Bajaj', 'Tanisha123', 'manager');