import sqlalchemy as sqla
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(os.getenv('MYSQL_CONNECTION2'))
        self.connection = self.engine.connect()

###Profile
    def get_profile_info(self, id : int):
        query = sqla.text("SELECT * FROM students WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        result = self.connection.execute(query).fetchone()._asdict()
        return result
    
    def get_profile_achivments(self, id : int):
        query = sqla.text("SELECT * FROM achievement WHERE student_id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        result = []
        for r in self.connection.execute(query).all():
            result.append(r._asdict())
        return result
        