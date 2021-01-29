import psycopg2
from psycopg2 import Error

        connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="FS104")


    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE users
          (
              id integer     NOT NULL,
          firstname varchar,
          lastname varchar,
          CONSTRAINT primary_key PRIMARY KEY (id)
          ); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
