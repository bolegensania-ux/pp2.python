import psycopg2

conn = psycopg2.connect(
    dbname = "my_first_db",
    user = "postgres",
    password = "BS150907",
    host = "localhost",
    port = "5432"
)

# in order to connect pyhton with pgAdmin4 we need to import psycopg2 