DROP TABLE instrumento;

CREATE TABLE instrumento (
  id_instrumento serial PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  preco FLOAT NOT NULL, 
  em_promocao BOOLEAN
);

CREATE TABLE vendedor (
  id_vendedor serial PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  telefone VARCHAR(25) NOT NULL,
  email VARCHAR(50)
);

INSERT INTO instrumento (nome, preco, em_promocao) VALUES
('Cavaquinho', 915.99, FALSE),
('Piano de Calda', 52099.98, TRUE),
('Contrabaixo', 4499.90, TRUE),
('Gaita', 200.99, FALSE);

INSERT INTO vendedor(nome, telefone, email) VALUES
('João Lee', '+55(81)996742896', 'joaumlee@multisom.com'),
('Roberto Carlos Ramos', '+55(28)981118852', 'betoramos27@multisom.com'),
('Silvana Salles', '+55(62)982768875', 'silsallesdf@multisom.com'),
('Alfeu Rodrigues', '+55(81)987998497', 'alfeuxrodrigues@multisom.com'),
('Santiago Rocha', '+55(81)984322765', 'santidrocha@gmail.com');

SELECT * FROM instrumento;
SELECT * FROM vendedor;

ALTER TABLE vendedor
ADD COLUMN email_2 VARCHAR(25)

UPDATE vendedor
SET email_2 = 'joaovitor_mxl@gmail.com'
WHERE id_vendedor = 1;

UPDATE vendedor
SET email_2 = 'robertinhoho@gmail.com'
WHERE id_vendedor = 2;

UPDATE vendedor
SET email_2 = 'sildoarrocha@gmail.com'
WHERE id_vendedor = 3;

UPDATE vendedor
SET email_2 = 'alfeurodrigues@gmail.com'
WHERE id_vendedor = 4;

UPDATE vendedor
SET email_2 = 'santibonhomme@gmail.com'
WHERE id_vendedor = 5;

-- Selecionar os instrumentos que não estão em promoção e com valor menor que 500:
SELECT * From instrumento WHERE em_promocao = FALSE AND preco < 500;
-- Selecionar instrumentos ordenados pelo nome em ordem alfabética:
SELECT nome from instrumento ORDER BY nome ASC
-- Selecionar os instrumentos com preços maiores que um determinado valor
SELECT * FROM instrumento WHERE preco > 1000;
-- Selecionar o nome e o estado de promoção dos instrumentos com preço superior a 100.00:
SELECT nome, em_promocao FROM instrumento WHERE preco > 100