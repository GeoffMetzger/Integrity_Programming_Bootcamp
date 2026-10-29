import psycopg2
from psycopg2 import sql

# Executing secure, injection-safe relational database engine configurations
def initialize_database_schema():
    # Establishing local connection parameters to our PostgreSQL instance
    connection = psycopg2.connect(
    dbname="integrity_bootcamp_db",
    user="postgres",
    password="",  # Ensure this parameter is explicitly typed
    host="localhost",
    port="5432"
)

    cursor = connection.cursor()
    
    # Constructing the master system logging table schema layout
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS application_logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMPTZ NOT NULL,
            service_origin VARCHAR(100) NOT NULL,
            status_code INT NOT NULL,
            traceback_active BOOLEAN NOT NULL
        );
    """)
    
    # Inserting structured tracking metrics securely using parameterized query markers
    insert_query = """
        INSERT INTO application_logs (timestamp, service_origin, status_code, traceback_active)
        VALUES (%s, %s, %s, %s);
    """
    log_data_payload = ("2026-10-25T09:23:00Z", "fastapi_ingestion_engine", 500, True)

    cursor.execute(insert_query, log_data_payload)
    connection.commit()

    print("Database Action: Schema initialized and secure payload record inserted successfully")
    cursor.close()
    connection.close()

initialize_database_schema()