from database.database import engine, Base

if __name__ == "__main__":
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")