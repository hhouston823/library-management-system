import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to the MySQL database")
            cursor = connection.cursor()
            return connection, cursor
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None, None