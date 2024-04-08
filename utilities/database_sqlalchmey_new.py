import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import urllib.parse


class Database:
    instance = None
    logger = logging.getLogger(__name__)

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Database, cls).__new__(cls)
            cls.instance.initialize()
        return cls.instance

    def initialize(self):

        try:
            DB_USERNAME = os.getenv('MYSQL_USER')
            DB_PASSWORD = urllib.parse.quote_plus(os.getenv('MYSQL_PASSWORD'))
            DB_HOST = os.getenv('MYSQL_HOST')
            DB_NAME = os.getenv('MYSQL_DB')

            # Creating an engine
            self.engine = create_engine(f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

            # Creating a session
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

        except Exception as e:
            self.logger.error(f"Error in creating session: {e}")
            raise
        finally:
            self.session.close()
            self.logger.info(f"Session closed")
