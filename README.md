# Ecommerce Database

Projeto acadêmico de banco de dados para e-commerce, com esquema SQL e interface de linha de comando em Python para operações CRUD e consultas relacionais.

## Resumo

Este repositório contém:

- Modelagem e criação do banco de dados em MariaDB/MySQL.
- Script Python para executar operações:
	- `SELECT`
	- `INSERT`
	- `UPDATE`
	- `DELETE`
	- `JOIN`
	- `CROSS JOIN`
	- Consulta aninhada

## Tecnologias

- Python 3.12+
- MySQL Connector Python (`mysql-connector-python`)
- MariaDB/MySQL (via XAMPP)
- phpMyAdmin (importação do banco)

## Estrutura do Projeto

```text
Ecommerce-DataBase-main/
	banco_de_dados.sql
	script.py
	README.md
```

## Requisitos

- Windows com XAMPP instalado.
- Serviço MySQL iniciado no XAMPP.
- Python instalado.

## Configuracao do Banco (XAMPP)

1. Abra o XAMPP Control Panel.
2. Inicie o serviço `MySQL`.
3. Acesse `http://localhost/phpmyadmin`.
4. Clique em `Importar` e selecione `banco_de_dados.sql`.
5. Execute a importação.

Isso criará o banco `seu_pai` e as tabelas utilizadas pelo script.

## Instalacao e Execucao

No terminal (PowerShell), dentro da pasta do projeto:

```powershell
cd C:\Users\W10\Downloads\Ecommerce-DataBase-main
```

### Opcao recomendada: ambiente virtual

```powershell
C:/msys64/mingw64/bin/python3.12.exe -m venv .venv_msys
C:/Users/W10/Downloads/Ecommerce-DataBase-main/.venv_msys/bin/python.exe -m pip install --upgrade pip
C:/Users/W10/Downloads/Ecommerce-DataBase-main/.venv_msys/bin/python.exe -m pip install mysql-connector-python
```

Executar o sistema:

```powershell
C:/Users/W10/Downloads/Ecommerce-DataBase-main/.venv_msys/bin/python.exe C:/Users/W10/Downloads/Ecommerce-DataBase-main/Ecommerce-DataBase-main/script.py
```

## Configuracao de Conexao

O arquivo `script.py` usa conexão local no padrão Windows/XAMPP:

```python
connection = mysql.connector.connect(
		host="127.0.0.1",
		port=3306,
		user="root",
		passwd="",
		db="seu_pai"
)
```

Se seu `root` tiver senha, ajuste o campo `passwd`.

## Como Testar Rapido

Com o sistema em execução:

1. Digite `1` para `SELECT`.
2. Informe uma tabela, por exemplo `cliente`.
3. Verifique se os dados aparecem sem erro.
4. Digite `0` para sair.

## Solucao de Problemas

### Erro: `ModuleNotFoundError: No module named 'mysql'`

O pacote foi instalado em outro interpretador Python.

Use o mesmo Python para instalar e executar:

```powershell
C:/Users/W10/Downloads/Ecommerce-DataBase-main/.venv_msys/bin/python.exe -m pip install mysql-connector-python
C:/Users/W10/Downloads/Ecommerce-DataBase-main/.venv_msys/bin/python.exe C:/Users/W10/Downloads/Ecommerce-DataBase-main/Ecommerce-DataBase-main/script.py
```

### Erro de conexao com banco

- Verifique se o MySQL do XAMPP está iniciado.
- Confirme se o banco `seu_pai` foi importado.
- Confira usuário/senha em `script.py`.

## Observacoes

- Projeto desenvolvido para fins didáticos.
- O script atual é interativo via terminal e focado em operações SQL.

## Integrantes e Documentacao

- Documento original do grupo:
	- https://docs.google.com/document/d/1K9XTfvARnPkj0bmLmrw6FmoY26Lv5vzudaaEyapuNHc/edit?usp=sharing
