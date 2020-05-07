# -*- coding: utf-8 -*-
"""Gtk ListStore."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    def __init__(self):
        self.con = sqlite3.connect('../../data/db.sqlite3')
        self.cur = self.con.cursor()

        self.revealer = builder.get_object(name='revealer')
        self.search_entry = builder.get_object(name='searchentry')

        self.liststore = builder.get_object(name='liststore')
        brazilian_states = self.populate_liststore()
        for state in brazilian_states:
            self.liststore.append(row=state)

    def populate_liststore(self):
        query = 'SELECT rowid, state FROM brazilian_states;'
        self.cur.execute(query)
        return self.cur.fetchall()

    def show_hide_search(self, widget):
        # Verificando se o botão está sendo exibido ou não.
        # get_reveal_child() retorna True ou False.
        show = self.revealer.get_reveal_child()

        # Laço de decisão altera o estado de exibição.
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)

    def search(self, widget):
        entry_text = widget.get_text()
        if entry_text:
            rows = self.find_rows(state=entry_text)
            self.liststore.clear()
            for row in rows:
                self.liststore.append(row=row)
        else:
            self.liststore.clear()

    def find_rows(self, state):
        query = 'SELECT rowid, state FROM brazilian_states WHERE state LIKE "%"||?||"%";'
        self.cur.execute(query, (state,))
        return self.cur.fetchall()

    def on_doble_click_row(self, TreeView, index, TreeViewColumn):
        TreeSelection = TreeView.get_selection()
        liststore, treeiter = TreeSelection.get_selected()
        value = liststore.get_value(iter=treeiter, column=1)
        self.search_entry.set_text(value)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
