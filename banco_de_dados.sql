CREATE DATABASE seu_pai;

USE seu_pai;

CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(50) NOT NULL,
    data_nasc DATE NOT NULL,
    telefone VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(30) NOT NULL
);

CREATE TABLE endereco (
    id_endereco INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    rua VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    CEP VARCHAR(50) NOT NULL,
    numero INT NOT NULL
);

CREATE TABLE parceiros (
    id_parceiros INT AUTO_INCREMENT PRIMARY KEY,
    cpf_cnpj VARCHAR(50),
    nome VARCHAR(50),
    tipo_conta VARCHAR(50),
    cod_banco INT NOT NULL,
    num_agencia INT NOT NULL,
    num_conta INT NOT NULL,
    telefone VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE armazem (
    id_armazem INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    cidade VARCHAR(50),
    capacidade INT NOT NULL
);

CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(100)
);

CREATE TABLE afiliado (
    id_afiliado INT AUTO_INCREMENT PRIMARY KEY,
    comissao DECIMAL(10, 2) NOT NULL,
    id_parceiros INT NOT NULL,
    FOREIGN KEY (id_parceiros) REFERENCES parceiros (id_parceiros)
);

CREATE TABLE vendedor (
    id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    id_parceiros INT NOT NULL,
    FOREIGN KEY (id_parceiros) REFERENCES parceiros (id_parceiros)
);

CREATE TABLE produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    qtd_estoque INT NOT NULL,
    id_categoria INT NOT NULL,
    id_vendedor INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria),
    FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor)
);

CREATE TABLE carrinho (
    id_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    status VARCHAR(30),
    data_hora_pagamento DATE NOT NULL,
    id_afiliado INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    FOREIGN KEY (id_afiliado) REFERENCES afiliado (id_afiliado)
);

CREATE TABLE avaliacao (
    id_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
    TITULO VARCHAR(50),
    comentario VARCHAR(50),
    nota INT NOT NULL,
    id_produto INT NOT NULL,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE parceiros_pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_parceiros INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    data DATE NOT NULL,
    FOREIGN KEY (id_parceiros) REFERENCES parceiros (id_parceiros)
);

CREATE TABLE armazem_produto (
    id_armazem_produto INT AUTO_INCREMENT  PRIMARY KEY,
    id_produto INT NOT NULL,
    id_armazem INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
    FOREIGN KEY (id_armazem) REFERENCES armazem (id_armazem)
);

CREATE TABLE carrinho_produto (
    id_carrinho_produto INT AUTO_INCREMENT  PRIMARY KEY,
    id_produto INT NOT NULL,
    id_carrinho INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
    FOREIGN KEY (id_carrinho) REFERENCES carrinho (id_carrinho)
);
