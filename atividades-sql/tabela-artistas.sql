CREATE TABLE gravadora (
  ID SERIAL PRIMARY KEY,
  nome VARCHAR(50) not NULL,
  sede VARCHAR(50) not NULL
);

CREATE TABLE artista (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  idade INT NOT NULL,
  gravadora_id INT,
  FOREIGN KEY (gravadora_id) REFERENCES gravadora(id)
);

CREATE TABLE album (
  ID SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  duracao FLOAT not NULL,
  artista_id INT,
  FOREIGN KEY (artista_id) REFERENCES artista(id)
);

INSERT INTO gravadora (nome, sede) VALUES
('Universal Music', 'Los Angeles'),
('Sony Music', 'Nova Iorque'),
('Warner Music', 'Londres'),
('Atlantic Records', 'Atlanta'),
('Capitol Records', 'Hollywood');

INSERT INTO artista (nome, idade, gravadora_id) VALUES
('John Doe', 28, 1),
('Jane Smith', 32, 2),
('Carlos Santana', 45, 3),
('Ariana Clarke', 22, 4),
('Michael Rivers', 40, 5);

INSERT INTO album (nome, duracao, artista_id) VALUES
('Hits of Summer', 42.5, 1),
('Dreams and Realities', 50.0, 2),
('Guitar Legends', 60.2, 3),
('Rise Up', 35.8, 4),
('The River Flows', 48.7, 5);

SELECT * FROM artista
INNER JOIN gravadora
ON gravadora.id = artista.gravadora_id;

SELECT * FROM album
RIGHT JOIN artista
ON artista.id = album.artista_id;
