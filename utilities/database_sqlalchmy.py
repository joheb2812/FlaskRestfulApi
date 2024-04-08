import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import urllib.parse


class Database:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        try:
            DB_USERNAME = os.getenv('MYSQL_USER')
            DB_PASSWORD = urllib.parse.quote_plus(os.getenv('MYSQL_PASSWORD'))
            DB_HOST = os.getenv('MYSQL_HOST')
            DB_NAME = os.getenv('MYSQL_DB')

            # Creating an engine
            self.engine = create_engine(f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

            # Creating a session
            # Session = sessionmaker(bind=self.engine)
            # print("type of session = ", type(Session))
            # self.session = Session()

        except Exception as e:
            self.logger.error(f"Error in creating session: {e}")
            raise
        # finally:
        #     if hasattr(self, 'session') and self.session:
        #         self.session.close()

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        # print("type of session = ", type(Session))
        return Session()
        # return sessionmaker(bind=self.engine)



db = Database()
