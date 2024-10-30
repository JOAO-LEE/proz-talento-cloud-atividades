CREATE TABLE gravadora (
  ID SERIAL PRIMARY KEY,
  nome VARCHAR(50) not NULL,
  sede VARCHAR(50) not NULL
)

CREATE TABLE artista (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  idade INT NOT NULL,
  gravadora_id INT,
  FOREIGN KEY (gravadora_id) REFERENCES gravadora(id)
)

CREATE TABLE album (
  ID SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  duracao FLOAT not NULL,
  artista_id INT,
  FOREIGN KEY (artista_id) REFERENCES artista(id)
)