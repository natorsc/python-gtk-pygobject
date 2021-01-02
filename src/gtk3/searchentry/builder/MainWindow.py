# -*- coding: utf-8 -*-
"""SearchEntry()."""

import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gio


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    revealer = Gtk.Template.Child(name='revealer')
    list_store = Gtk.Template.Child(name='list_store')
    search_entry = Gtk.Template.Child(name='search_entry')

    def __init__(self, **kwargs):
        super().__init__(application=kwargs['application'])

        self.cur = kwargs['con'].cursor()

        brazilian_states = self.get_brazilian_states()
        for state in brazilian_states:
            self.list_store.append(row=state)

        self.show_all()

    @Gtk.Template.Callback()
    def set_entry_text(self, tree_view, path, column):
        list_store = tree_view.get_model()
        self.search_entry.set_text(text=list_store[path][1])

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
            self.list_store.clear()
            # Adicionando novos valores.
            for row in rows:
                self.list_store.append(row=row)
        else:
            # Caso o entry esteja vazio.
            self.list_store.clear()

    def get_brazilian_states(self):
        query = 'SELECT rowid, state FROM brazilian_states;'
        data = self.cur.execute(query)
        return data.fetchall()

    def search_state(self, state):
        query = 'SELECT rowid, state FROM brazilian_states WHERE state LIKE "%"||?||"%";'
        data = self.cur.execute(query, (state,))
        return data.fetchall()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        self.con = sqlite3.connect('../../../data/database/brazilian_states.sqlite3')

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self, con=self.con)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

        # Fechando a conexão com o banco de dados.
        self.con.close()


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
