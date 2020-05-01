# -*- coding: utf-8 -*-
"""GTK SearchEntry."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Pango


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('../data/db.sqlite3')
        self.cur = self.con.cursor()

        self.set_title(title='GTK SearchEntry')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        label = Gtk.Label.new(
            str='Comece a digitar para pesquisar\n'
                '2 cliques para selecionar o item.'
        )
        vbox.add(widget=label)

        self.search_entry = Gtk.SearchEntry.new()
        self.search_entry.connect('search-changed', self.search)
        vbox.add(widget=self.search_entry)

        cols = ('ID', 'Estados')

        self.liststore = Gtk.ListStore(int, str)

        treeview = Gtk.TreeView(model=self.liststore)
        treeview.connect('row-activated', self.on_doble_click_row)
        for i, col in enumerate(cols):
            cellrender = Gtk.CellRendererText.new()
            if i == 0:
                cellrender.props.weight_set = True
                cellrender.props.weight = Pango.Weight.BOLD

            treeviewcolumn = Gtk.TreeViewColumn(title=col, cell_renderer=cellrender, text=i)
            treeview.append_column(column=treeviewcolumn)

        vbox.pack_start(child=treeview, expand=True, fill=True, padding=0)

    def on_doble_click_row(self, TreeView, index, TreeViewColumn):
        TreeSelection = TreeView.get_selection()
        liststore, treeiter = TreeSelection.get_selected()
        value = liststore.get_value(iter=treeiter, column=1)
        self.search_entry.set_text(value)

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


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
