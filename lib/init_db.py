from database import initialize_database
from worker import Worker  
from job import Job      

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
