import sqlalchemy as sqla
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(os.getenv('MYSQL_CONNECTION2'))
        self.connection = self.engine.connect()
    
    def get_profile_info(self, id):
        query = sqla.text("SELECT * FROM students WHERE id = 1")
        result = self.connection.execute(query).fetchone()._asdict()
        print(result['firstname'])

if __name__ == "__main__":
    Database().get_profile_info(123)