# -*- coding: utf-8 -*-
"""CRUD basico com SQLite 3."""

import sqlite3


class ConnectDB:

    def __init__(self):
        self.con = sqlite3.connect('../../../data/database/crud.sqlite3')

        # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
        self.cur = self.con.cursor()

        # Remover tabela.
        self.drop_table(table_name='notes')

        # Verificando se a tabela já existe.
        if not self.check_table_exists(table_name='notes'):
            # Criando a tabela.
            self.create_table()

    def check_table_exists(self, table_name):
        query = f'''SELECT name FROM sqlite_master WHERE type='table' AND name = ?;'''
        self.cur.execute(query, (table_name,))
        return self.cur.fetchone()

    def create_table(self):
        """Cria a tabela caso a mesma não exista."""
        query = '''CREATE TABLE IF NOT EXISTS `notes` (
        `note_id`   INTEGER         NOT NULL,
        `note`      VARCHAR(100)    NOT NULL,
        PRIMARY KEY(note_id)
        );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela criada com sucesso [!]')

    def drop_table(self, table_name):
        query = f'DROP TABLE IF EXISTS {table_name};'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao remover a tabela [x]: {e}')
        else:
            # Commit para registrar a operação/transação no banco.
            self.con.commit()
            print('\n[!] Tabela removida com sucesso [!]')

    def insert_note(self, data):
        query = f'''INSERT INTO notes (note) VALUES (?);'''
        try:
            self.cur.execute(query, (data,))
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao inserir registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]')

    def read_notes(self):
        query = f'SELECT * FROM notes;'
        self.cur.execute(query)
        return self.cur.fetchall()

    def update_note(self, data, note_id):
        query = f'''UPDATE notes SET note = ? WHERE note_id = ?;'''
        try:
            self.cur.execute(query, (data, note_id))
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha na alteração do registro [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]')

    def delete_note(self, note_id):
        query = 'DELETE FROM notes WHERE note_id = ?;'
        try:
            self.cur.execute(query, (note_id,))
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

    # Inserindo um novo registro.
    # note = 'Nota'
    # database.insert_note(data=note)

    # Lendo todos os registros (sem limit).
    # print('\n')
    # print(database.read_notes())

    # Alterando um registro.
    # print('\nANTES da alteração:')
    # print(database.read_notes())
    # data = ('Nota atualizada de novo')
    # database.update_note(data=data, note_id=2)
    # print('\nDEPOIS da alteração:')
    # print(database.read_notes())
    # print('----')

    # Removendo registro da tabela.
    # print('\nANTES da remoção:')
    # print(database.read_notes())
    # database.delete_note(note_id=2)
    # print('\nDEPOIS da remoção:')
    # print(database.read_notes())
    # print('----')

    # Fechando conexão com o banco.
    database.con.close()
