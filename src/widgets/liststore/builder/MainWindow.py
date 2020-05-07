# -*- coding: utf-8 -*-
"""GTK ListStore."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'
    con = sqlite3.connect('../../data/db.sqlite3')
    cur = con.cursor()

    revealer = Gtk.Template.Child(name='revealer')
    search_entry = Gtk.Template.Child(name='searchentry')
    liststore = Gtk.Template.Child(name='liststore')

    def __init__(self):
        super().__init__()
        brazilian_states = self.populate_liststore()
        for state in brazilian_states:
            self.liststore.append(row=state)

    def populate_liststore(self):
        query = 'SELECT rowid, state FROM brazilian_states;'
        self.cur.execute(query)
        return self.cur.fetchall()

    def find_rows(self, state):
        query = 'SELECT rowid, state FROM brazilian_states WHERE state LIKE "%"||?||"%";'
        self.cur.execute(query, (state,))
        return self.cur.fetchall()

    @Gtk.Template.Callback()
    def show_hide_search(self, widget):
        show = self.revealer.get_reveal_child()
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)

    @Gtk.Template.Callback()
    def search(self, widget):
        entry_text = widget.get_text()
        if entry_text:
            rows = self.find_rows(state=entry_text)
            self.liststore.clear()
            for row in rows:
                self.liststore.append(row=row)
        else:
            self.liststore.clear()

    @Gtk.Template.Callback()
    def on_doble_click_row(self, TreeView, index, TreeViewColumn):
        TreeSelection = TreeView.get_selection()
        liststore, treeiter = TreeSelection.get_selected()
        value = liststore.get_value(iter=treeiter, column=1)
        self.search_entry.set_text(value)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
