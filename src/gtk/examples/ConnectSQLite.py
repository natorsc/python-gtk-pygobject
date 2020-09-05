# -*- coding: utf-8 -*-
"""CRUD basico com SQLite 3."""

import sqlite3


class ConnectDB:

    def __init__(self):
        if __name__ == '__main__':
            self.con = sqlite3.connect('../../../files/databases/gtk/devdb.sqlite3')
        else:
            self.con = sqlite3.connect('../../../files/assets/databases/tkinter/db.sqlite3')

        # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

        # Remover tabela.
        # self.drop_table(table='table_name')

        # Criando a tabela.
        self.create_table_user()

    def create_table_user(self):
        """Cria a tabela caso a mesma não exista."""
        query = '''CREATE TABLE IF NOT EXISTS `user` (
        `user_id`   INTEGER         NOT NULL,
        `name`      VARCHAR(100)    NOT NULL,
        `age`       INTEGER(3)      NOT NULL,
        `gender`    VARCHAR(10)     NOT NULL,
        PRIMARY KEY(user_id)
        );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela criada com sucesso [!]')

    def drop_table(self, table):
        """Remove uma tabela.

        :param table: (str) Nome da tabela que se deseja remover.
        """
        query = f'DROP TABLE IF EXISTS {table};'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao remover a tabela [x]: {e}')
        else:
            # Commit para registrar a operação/transação no banco.
            self.con.commit()
            print('\n[!] Tabela removida com sucesso [!]')

    def insert_row(self, data):
        """Adiciona uma nova linha na tabela.

        :param data: (tuple) Tupla contendo os dados.
        """
        query = f'''INSERT INTO user (name, age, gender) VALUES (?, ?, ?);'''
        try:
            self.cur.execute(query, data)
        except Exception as e:
            # rollback reverte/desfaz a operação.
            self.con.rollback()
            print('\n[x] Falha ao inserir registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]')

    def find_rows(self, table, limit=5):
        """Consulta todos os registros da tabela.

        Utilizando ``limit`` para evitar consultas longas de mais.

        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.

        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = f'SELECT * FROM {table} LIMIT ?;'
        self.cur.execute(query, (limit,))
        return self.cur.fetchall()

    def find_by_id(self, rowid):
        """Consulta o registro pela id.

        :param rowid: (int) id do usuário que se deseja consultar.

        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        query = 'SELECT * FROM users WHERE user_id = ?;'
        self.cur.execute(query, (rowid,))
        return self.cur.fetchone()

    def find_by_name(self, name):
        """Busca usuário pelo nome.

        :param name: (str) Nome que se deseja pesquisar.
        Está sendo utilizado ``%`` para que a pesquisa também inclua
        resultados que contenham trechos do nome que foi passado.

        :return: É retornada uma lista.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = f'SELECT * FROM users WHERE UPPER(name) LIKE UPPER(?);'
        self.cur.execute(query, ('%' + name + '%',))
        return self.cur.fetchall()

    def change_row(self, data):
        """Altera uma linha da tabela com base na id.

        :param data: (tuple) Tupla contendo os novos dados e a rowind
        onde os dados serão inseridos.
        """
        query = f'''UPDATE users SET name = ?, age = ?, gender = ? 
        WHERE user_id = ?;'''
        try:
            self.cur.execute(query, data)
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha na alteração do registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]')

    def remove_row(self, rowid):
        """Remove uma linha da tabela com base na id.

        :param rowid: (id) id da linha que se deseja remover.
        """
        query = 'DELETE FROM users WHERE user_id = ?;'
        try:
            self.cur.execute(query, (rowid,))
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao remover registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]')


if __name__ == '__main__':
    # Criando a conexão com o banco.
    database = ConnectDB()

    # Inserindo um registro tabela.
    # user = ('Renato', 35, 'Masculino')
    # database.insert_row(data=user)

    # Consultando com filtro.
    # print('\n')
    # print(database.find_by_name(name='renato'))

    # Consultando todos (limit=10).
    # print(database.find_rows(table='users', limit=10))
    # print('----')

    # Alterando registro da tabela.
    # print('\nANTES da alteração:')
    # print(database.find_by_id(rowid=1))
    # data = ('Rafaela', 50, 'Feminino', 1)
    # database.change_row(data=data)
    # print('\nDEPOIS da alteração:')
    # print(database.find_by_id(rowid=1))
    # print('----')

    # Removendo registro da tabela.
    # print('\nANTES da remoção:')
    # print(database.find_rows(table='users'))
    # database.remove_row(rowid=2)
    # print('\nDEPOIS da remoção:')
    # print(database.find_rows(table='users'))
    # print('----')

    # Fechando conexão com o banco.
    database.con.close()
