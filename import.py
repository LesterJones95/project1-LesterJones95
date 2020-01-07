import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    #db.execute("DROP TABLE books")

    # note some isbn _num have chars, and apperently some pub_years also
    db.execute("CREATE TABLE books(id SERIAL PRIMARY KEY, ISBN_number VARCHAR NOT NULL, \
     title VARCHAR NOT NULL, author VARCHAR NOT NULL ,publication_year VARCHAR NOT NULL)")
    print("Created Table: books")
    db.commit()

    for isbn, title, author, publication in reader:
        db.execute("INSERT INTO books (ISBN_number, title, author, publication_year) VALUES (:ISBN_number, :title, :author, :publication_year)",
        {"ISBN_number":isbn, "author":author, "title":title ,"publication_year":publication})

        print(f"Added book from {title} to the database")
    #save the changes I made
    db.commit()

if(__name__ == "__main__"):
    main()
