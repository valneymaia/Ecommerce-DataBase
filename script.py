import mysql.connector

connection = mysql.connector.connect(
host="127.0.0.1",
port=3306,
user="root",
passwd="",
db="seu_pai"
)


cursor = connection.cursor()

def display():
  string = """+----------------------+
| Tabelas no banco de dados   |
------------------------
| afiliado             |
| armazem              |
| armazem_produto      |
| avaliacao            |
| carrinho             |
| carrinho_produto     |
| categoria            |
| cliente              |
| endereco             |
| parceiros            |
| parceiros_pagamentos |
| produto              |
| vendedor             |
------------------------
[1] SELECT
[2] INSERT
[3] UPDATE
[4] DELETE
[5] JOIN
[6] CONSULTA ANINHADA
[7] CROSS JOIN"""

  print(string)
  

def num_columns():
    query = "SELECT COUNT(*) FROM information_schema.columns WHERE table_name= 'cliente' "
    cursor.execute(query)
    
    col = cursor.fetchall()
    
    col = int(col[-1][-1])
    print(col)
    
    
def auto_insert():
    cont = 1
    index = 0
    n1 = 20000000
    tel = 90000000
    agencia = 100
    conta = 10000
    preco = 50.00
    status = ['finalizado', 'pendente', 'pendente', 'cancelado', 'estornado', 'pendente', 'pendente', 'estornado',
              'finalizado', 'finalizado']
    

    for i in range(1, 11):
        string = f'INSERT INTO cliente  VALUES ("", "nome_{cont}", "{n1}", "2020-01-{cont}", "{tel}", "email_{cont}", "senha_{cont}")'
        cursor.execute(string)
        connection.commit()
     
        string = f'INSERT INTO endereco VALUES ("", "{cont}", "rua_{cont}", "cidade_{cont}", "cep_{cont}", "numero_{cont}")'
        cursor.execute(string)
        connection.commit()
        
        string = f'INSERT INTO parceiros VALUES ("", "cpf_cnpj_{cont}", "nome_{cont}", "corrente", "2001", "{agencia}", "{conta}", "{tel}", "email_{cont}")'
        cursor.execute(string)
        connection.commit()
        
        string = f'INSERT INTO armazem VALUES ("", "nome_{cont}", "cidade_{cont}", "{cont + 10}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO categoria VALUES ("", "nome_{cont}", "descricao_{cont}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO afiliado VALUES ("", "20.00", "{cont}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO vendedor VALUES ("", "{cont}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO produto VALUES ("", "nome_{cont}", "{preco}", "{cont}", "{cont}", "{cont}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO carrinho VALUES ("", "{cont}", "{preco * 10}", "{status[index % 10]}", "2022-10-{cont:02d}", "{cont}")'
        cursor.execute(string)
        connection.commit()

        string = f'INSERT INTO avaliacao VALUES ("", "titulo_{cont}", "comentario_{cont}", "{5}", "{cont}", "{cont}")'
        cursor.execute(string)
        connection.commit()
        
        string = f'INSERT INTO parceiros_pagamentos VALUES ("", "{cont}", "{preco * 8}", "2022-10-{cont:02d}")'
        cursor.execute(string)
        connection.commit()
        
        string = f'INSERT INTO armazem_produto VALUES ("", "{cont}", "{cont}", "{cont + 4}")'
        cursor.execute(string)
        connection.commit()
        
        string = f'INSERT INTO carrinho_produto VALUES ("", "{cont}", "{cont}", "{cont + 5}")'
        cursor.execute(string)
        connection.commit()
        
        cont += 1
        n1 += 100
        tel += 100
        agencia += 10
        conta += 50
        preco += 50
        index += 1
    connection.commit()

    
def insert():
  
  dados = list()
  table = str(input("\nInserir em qual tabela? "))

  try:
    cursor.execute(f"SELECT * FROM {table}")
    cursor.fetchall()
  
    field_names = [i[0] for i in cursor.description]
    insert_fields = [i for i in field_names if i != f"id_{table}"]

    for i in insert_fields:
      dado = str(input(f"{i}: "))
      dado = "'" + dado + "'"
      dados.append(dado)

    values_by_field = {}
    for i in range(len(insert_fields)):
      values_by_field[insert_fields[i]] = dados[i].strip("'")

    if table == "produto":
      id_categoria = values_by_field.get("id_categoria")
      id_vendedor = values_by_field.get("id_vendedor")

      cursor.execute("SELECT 1 FROM categoria WHERE id_categoria = %s", (id_categoria,))
      if not cursor.fetchone():
        print("Erro: categoria inexistente. Cadastre primeiro em 'categoria' e use um id_categoria valido.")
        return

      cursor.execute("SELECT 1 FROM vendedor WHERE id_vendedor = %s", (id_vendedor,))
      if not cursor.fetchone():
        print("Erro: vendedor inexistente. Cadastre primeiro em 'vendedor' e use um id_vendedor valido.")
        return
    
    string = f'INSERT INTO {table} ( {", ".join(insert_fields)} ) VALUES ( {", ".join(dados)} )'
    
    cursor.execute(string)
    cursor.fetchall() 
    connection.commit()
    print("Elemento inserido com sucesso.")
    
  except mysql.connector.IntegrityError as ex:
    if ex.errno == 1452:
      print("Erro de chave estrangeira: verifique se os IDs informados existem nas tabelas relacionadas.")
    else:
      print(ex)
  except Exception as ex:
    print(ex)


def select():

  table = str(input("Realizar o select em qual tabela? "))
  print("\n")
  
  try:
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()

    for x in result:
      print(x)
    
  except Exception as ex:
    print(ex)


def delete():
  
  table = str(input("Realizar o delete em qual tabela? "))
  print("\n")
  
  try:
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    for x in result:
      print(x)

    id = int(input("Qual id deseja deletar? "))
    cursor.execute(f"DELETE FROM {table} WHERE id_{table} = {id}")
    connection.commit()
    print("Elemento deletado com sucesso.")
    
  except Exception as ex:
    print(ex)
    
    
def update():
  dados = list()
  table = str(input("Realizar o update em qual tabela? "))
  print("\n")
  
  try:
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    for x in result:
      print(x)
      
    id = int(input("Qual id deseja atualizar? "))
    cursor.execute(f"SELECT * FROM {table}")
    cursor.fetchall()
  
    field_names = [i[0] for i in cursor.description]
    update_fields = [i for i in field_names if i != f"id_{table}"]

    for i in update_fields:
      dado = str(input(f"{i}: "))
      dado = "'" + dado + "'"
      dados.append(dado)
      
    for i in range(len(update_fields)):
      string = f"UPDATE {table} SET {update_fields[i]} = {dados[i]} WHERE id_{table} = {id}"
      cursor.execute(string)
      connection.commit()
    
  except Exception as ex:
    print(ex)
    

def join():
  join_type = str(input("Qual join deseja realizar? "))
  table1 = str(input("Qual a primeira tabela? "))
  table2 = str(input("Qual a segunda tabela? "))
  
  try:
    cursor.execute(f"SELECT * FROM {table1} {join_type} {table2} ON {table1}.id_{table1} = {table2}.id_{table2}")
    result = cursor.fetchall()
    for x in result:
      print(x)
  except Exception as ex:
    print(ex)
  
def cross_join():
  table1 = str(input("Qual a primeira tabela? "))
  table2 = str(input("Qual a segunda tabela? "))
  
  try:
    cursor.execute(f"SELECT * FROM {table1} CROSS JOIN {table2}")
    result = cursor.fetchall()
    for x in result:
      print(x)
  except Exception as ex:
    print(ex)
  

def consulta_aninhada():
  

  try:
    cursor.execute(f"SELECT produto.nome, avaliacao.titulo FROM produto, avaliacao WHERE avaliacao.id_produto IN (SELECT id_produto FROM avaliacao)")
    #cursor.execute(f"SELECT * FROM {ext_table} WHERE id_{ext_table} IN (SELECT id_{ext_table} FROM {int_table})")
    result = cursor.fetchall()

    if not result:
      print("Sem resultados. Cadastre dados em 'produto' e 'avaliacao' para testar esta consulta.")
      return

    for item in result[:10]:
      print(item)
  except Exception as ex:
    print(ex)
  

def main():
  display()
  
  while True:
    esc = str(input("\nQual operação realizar? [0 para sair] "))
    
    if esc == '1':
      select()
    if esc == '2':
      insert()
    if esc == '3':
      update()
    if esc == '4':
      delete()
    if esc == '5':
      join()
    if esc == '6':
      consulta_aninhada()
    if esc== '7':
      cross_join()
    if esc == '0':
      break
    
"""
def main():
  auto_insert()
"""
main()
