import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # note some isbn _num have chars, and apperently some pub_years also
    db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, \
     password VARCHAR NOT NULL)")
    print("Created Table: users")
    db.commit()

if(__name__ == "__main__"):
    main()
