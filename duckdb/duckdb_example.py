import duckdb

# Connect to an in-memory database
con = duckdb.connect(":memory:")

# Create a table
con.execute("CREATE SEQUENCE IF NOT EXISTS fruit_seq START 1;")
con.execute("""
    CREATE TABLE IF NOT EXISTS fruits (
        id BIGINT PRIMARY KEY DEFAULT nextval('fruit_seq'),
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
""")

# Insert some data
con.execute("""
    INSERT INTO fruits (name, price)
    VALUES ('Apples', 1.20),
           ('Bananas', 0.80),
           ('Cherrys', 1.50)
""")

# Select all rows
rows = con.execute("SELECT * FROM fruits").fetchall()
for row in rows:
    print(row)

# Update a row
con.execute("UPDATE fruits SET price = 1.30 WHERE id = 2")

# Select all rows again
rows = con.execute("SELECT * FROM fruits").fetchall()
for row in rows:
    print(row)

# Delete a row
con.execute("DELETE FROM fruits WHERE id = 3")

# Select all rows again
rows = con.execute("SELECT * FROM fruits").fetchall()
for row in rows:
    print(row)

# Create a schema
con.execute("""
    CREATE SCHEMA IF NOT EXISTS my_schema
""")

# Use the schema
con.execute("USE my_schema")

# Create a table within the schema
con.execute("CREATE SEQUENCE IF NOT EXISTS employee_seq START 1;")
con.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id BIGINT PRIMARY KEY DEFAULT nextval('employee_seq'),
        name TEXT NOT NULL,
        salary REAL NOT NULL
    )
""")

# Insert some data
con.execute("""
    INSERT INTO employees (name, salary)
    VALUES ('Alice', 50000.00),
           ('Bob', 60000.00),
           ('Charlie', 70000.00)
""")

# Select all rows
rows = con.execute("SELECT * FROM employees").fetchall()
for row in rows:
    print(row)

# Update a row
con.execute("UPDATE employees SET salary = 65000.00 WHERE id = 2")

# Select all rows again
rows = con.execute("SELECT * FROM employees").fetchall()
for row in rows:
    print(row)

# Delete a row
con.execute("DELETE FROM employees WHERE id = 2")

# Select all rows again
rows = con.execute("SELECT * FROM employees").fetchall()
for row in rows:
    print(row)

# Close the connection
con.close()
