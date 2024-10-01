import sqlalchemy as sqla
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(os.getenv('MYSQL_CONNECTION2'))
        self.connection = self.engine.connect()

    def get_profile_info(self, id : int):
        query = sqla.text("SELECT * FROM students WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", int(id)))
        result = self.connection.execute(query).fetchone()._asdict()
        return result