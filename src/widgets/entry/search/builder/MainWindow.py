# -*- coding: utf-8 -*-
"""GTK SearchEntry, realizando pesquisas."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'
    con = sqlite3.connect('../../../data/db.sqlite3')
    cur = con.cursor()

    revealer = Gtk.Template.Child(name='revealer')
    liststore = Gtk.Template.Child(name='liststore')

    def __init__(self):
        super().__init__()
        brazilian_states = self.get_brazilian_states()
        for state in brazilian_states:
            self.liststore.append(row=state)

    @Gtk.Template.Callback()
    def show_hide_search(self, widget):
        show = self.revealer.get_reveal_child()
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)

    @Gtk.Template.Callback()
    def on_search_changed(self, widget):
        # Pegando o texto do entry.
        entry_text = widget.get_text()
        if entry_text:
            # Buscando no banco.
            rows = self.search_state(state=entry_text)
            # Limpando os valores existentes no `Gtk.ListStore()`.
            self.liststore.clear()
            # Adicionando novos valores.
            for row in rows:
                self.liststore.append(row=row)
        else:
            # Caso o entry esteja vazio.
            self.liststore.clear()

    def get_brazilian_states(self):
        query = 'SELECT rowid, state FROM brazilian_states;'
        data = self.cur.execute(query)
        return data.fetchall()

    def search_state(self, state):
        query = 'SELECT rowid, state FROM brazilian_states WHERE state LIKE "%"||?||"%";'
        data = self.cur.execute(query, (state,))
        return data.fetchall()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
