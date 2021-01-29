import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="exercises")

    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    record = cursor.fetchall()
    print("Result ", record)

    # Executing a SQL query to update table
    update_query = """Update mobile set price = 1500 where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record updated successfully ")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    print("Result ", cursor.f
    