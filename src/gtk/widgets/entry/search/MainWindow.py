# -*- coding: utf-8 -*-
"""GTK SearchEntry, realizando pesquisas."""
import sqlite3

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Pango, GObject


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('../../data/db.sqlite3')
        self.cur = self.con.cursor()

        self.set_title(title='GTK SearchEntry, realizando pesquisas')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='GTK SearchEntry, realizando pesquisas')
        headerbar.set_subtitle(subtitle='GTK SearchEntry, realizando pesquisas')
        headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=headerbar)

        btn_search = Gtk.Button.new_from_icon_name(
            icon_name='system-search-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        btn_search.connect('clicked', self.show_hide_search)
        headerbar.pack_start(child=btn_search)

        self.revealer = Gtk.Revealer.new()
        vbox.pack_start(child=self.revealer, expand=False, fill=True, padding=0)

        self.search_entry = Gtk.SearchEntry.new()
        self.search_entry.connect('search-changed', self.on_search_changed)
        self.revealer.add(widget=self.search_entry)

        # Janela com rolagem onde será adicionado o Gtk.TreeView().
        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_end(child=scrolledwindow, expand=True, fill=True, padding=0)

        # Criando um modelo com `Gtk.ListStore()`.
        self.liststore = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])

        # Adicionando os dados no `Gtk.ListStore()`.
        for state in self.get_brazilian_states():
            self.liststore.append(row=state)

        # Criando um `Gtk.TreeView()`.
        treeview = Gtk.TreeView.new_with_model(model=self.liststore)
        scrolledwindow.add(widget=treeview)

        # Nome das colunas (title).
        cols = ('ID', 'Estados')
        for i, col in enumerate(cols):
            # Criando um rederizador com para o tipo de dado que será exibido.
            cellrender = Gtk.CellRendererText.new()

            # Configurando o rederizador da primeira coluna.
            if i == 0:
                cellrender.props.weight_set = True
                cellrender.props.weight = Pango.Weight.BOLD

            # Criando a coluna.
            treeviewcolumn = Gtk.TreeViewColumn(
                # Titulo da coluna.
                title=col,
                # Rederizador que será utilizado na coluna.
                cell_renderer=cellrender,
                # Posição (index) da coluna.
                text=i,
            )

            # Definindo que a coluna pode ordenar o conteúdo.
            treeviewcolumn.set_sort_column_id(sort_column_id=i)

            # Adicionando a coluna no `Gtk.TreeView()`.
            treeview.append_column(column=treeviewcolumn)

    def show_hide_search(self, widget):
        show = self.revealer.get_reveal_child()
        if show:
            self.revealer.set_reveal_child(reveal_child=False)
        else:
            self.revealer.set_reveal_child(reveal_child=True)

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
