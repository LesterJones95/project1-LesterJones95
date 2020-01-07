CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  username VARCHAR NOT NULL,
  password VARCHAR NOT NULL);

INSERT INTO users(username, password) VALUES ('LesterJones95', 'project1_cs50');
