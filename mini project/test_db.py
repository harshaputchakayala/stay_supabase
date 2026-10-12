import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

db_url = os.getenv("DATABASE_URL")

print("Connecting to Cloud Database...")

try:
    # Create database engine
    engine = create_engine(db_url)
    
    # Open connection and execute test query
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.fetchone()
        print("\n[SUCCESS] Connected to Supabase PostgreSQL!")
        print(f"PostgreSQL Version: {db_version[0]}\n")

except Exception as e:
    print("\n[ERROR] Connection failed!")
    print(e)
