

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
# import psycopg2

try:
    # Define the connection string
    connection_string = "postgresql://consultants:WelcomeItc@2022@ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"

    # Create an SQLAlchemy engine
    engine = create_engine(connection_string)

    # Connect to the PostgreSQL database
    connection = engine.connect()

    # Define the SQL query to select data from the table
    sql_query = "SELECT * FROM your_table_name;"

    # Execute the SQL query and fetch all the rows
    result = connection.execute(sql_query).fetchall()

    # Loop through the rows and print each row
    for row in result:
        print(row)

    # Close the connection
    connection.close()

except SQLAlchemyError as e:
    print("Error connecting to PostgreSQL database:", e)
