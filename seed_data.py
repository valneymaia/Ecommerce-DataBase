import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="",
        db="seu_pai",
    )


def reset_tables(cursor):
    tables = [
        "carrinho_produto",
        "armazem_produto",
        "parceiros_pagamentos",
        "avaliacao",
        "carrinho",
        "produto",
        "vendedor",
        "afiliado",
        "categoria",
        "armazem",
        "endereco",
        "cliente",
        "parceiros",
    ]

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    for table in tables:
        cursor.execute(f"TRUNCATE TABLE {table}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")


def seed_data(cursor):
    clientes = [
        ("Ana Silva", "11111111111", "1998-01-10", "11999990001", "ana@email.com", "senha123"),
        ("Bruno Lima", "22222222222", "1997-03-22", "11999990002", "bruno@email.com", "senha123"),
        ("Carla Souza", "33333333333", "1995-07-05", "11999990003", "carla@email.com", "senha123"),
    ]
    cursor.executemany(
        "INSERT INTO cliente (nome, cpf, data_nasc, telefone, email, senha) VALUES (%s, %s, %s, %s, %s, %s)",
        clientes,
    )

    enderecos = [
        (1, "Rua A", "Sao Paulo", "01001000", 10),
        (2, "Rua B", "Sao Paulo", "01002000", 20),
        (3, "Rua C", "Sao Paulo", "01003000", 30),
    ]
    cursor.executemany(
        "INSERT INTO endereco (id_cliente, rua, cidade, CEP, numero) VALUES (%s, %s, %s, %s, %s)",
        enderecos,
    )

    parceiros = [
        ("12345678000190", "Mercado XPTO", "corrente", 2001, 101, 12345, "11988880001", "parceiro1@email.com"),
        ("98765432000190", "Distribuidora Y", "corrente", 2001, 102, 12346, "11988880002", "parceiro2@email.com"),
    ]
    cursor.executemany(
        "INSERT INTO parceiros (cpf_cnpj, nome, tipo_conta, cod_banco, num_agencia, num_conta, telefone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        parceiros,
    )

    categorias = [
        ("Frutas", "Alimentos frescos"),
        ("Bebidas", "Bebidas em geral"),
        ("Limpeza", "Produtos de limpeza"),
    ]
    cursor.executemany(
        "INSERT INTO categoria (nome, descricao) VALUES (%s, %s)",
        categorias,
    )

    afiliados = [
        (10.00, 1),
        (12.50, 2),
    ]
    cursor.executemany(
        "INSERT INTO afiliado (comissao, id_parceiros) VALUES (%s, %s)",
        afiliados,
    )

    vendedores = [
        (1,),
        (2,),
    ]
    cursor.executemany(
        "INSERT INTO vendedor (id_parceiros) VALUES (%s)",
        vendedores,
    )

    produtos = [
        ("Banana", 5.00, 70, 1, 1),
        ("Suco de Laranja", 8.90, 40, 2, 2),
        ("Detergente", 3.50, 120, 3, 1),
    ]
    cursor.executemany(
        "INSERT INTO produto (nome, preco, qtd_estoque, id_categoria, id_vendedor) VALUES (%s, %s, %s, %s, %s)",
        produtos,
    )

    avaliacoes = [
        ("Muito bom", "Produto fresco", 5, 1, 1),
        ("Bom", "Chegou rapido", 4, 2, 2),
        ("Regular", "Atendeu", 3, 3, 3),
    ]
    cursor.executemany(
        "INSERT INTO avaliacao (titulo, comentario, nota, id_produto, id_cliente) VALUES (%s, %s, %s, %s, %s)",
        avaliacoes,
    )

    carrinhos = [
        (1, 25.00, "finalizado", "2026-03-20", 1),
        (2, 17.80, "pendente", "2026-03-20", 2),
    ]
    cursor.executemany(
        "INSERT INTO carrinho (id_cliente, preco, status, data_hora_pagamento, id_afiliado) VALUES (%s, %s, %s, %s, %s)",
        carrinhos,
    )

    parceiros_pagamentos = [
        (1, 100.00, "2026-03-20"),
        (2, 150.00, "2026-03-20"),
    ]
    cursor.executemany(
        "INSERT INTO parceiros_pagamentos (id_parceiros, valor, data) VALUES (%s, %s, %s)",
        parceiros_pagamentos,
    )

    armazens = [
        ("CD Zona Sul", "Sao Paulo", 500),
        ("CD Zona Norte", "Sao Paulo", 450),
    ]
    cursor.executemany(
        "INSERT INTO armazem (nome, cidade, capacidade) VALUES (%s, %s, %s)",
        armazens,
    )

    armazem_produtos = [
        (1, 1, 50),
        (2, 1, 30),
        (3, 2, 70),
    ]
    cursor.executemany(
        "INSERT INTO armazem_produto (id_produto, id_armazem, quantidade) VALUES (%s, %s, %s)",
        armazem_produtos,
    )

    carrinho_produtos = [
        (1, 1, 5),
        (2, 2, 2),
        (3, 1, 3),
    ]
    cursor.executemany(
        "INSERT INTO carrinho_produto (id_produto, id_carrinho, quantidade) VALUES (%s, %s, %s)",
        carrinho_produtos,
    )


def main():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        reset_tables(cursor)
        seed_data(cursor)
        connection.commit()
        print("Base populada com sucesso.")
    except Exception as ex:
        connection.rollback()
        print(f"Erro ao popular base: {ex}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
