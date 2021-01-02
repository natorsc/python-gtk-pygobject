# -*- coding: utf-8 -*-
"""Gtk.TreeView(), Gtk.TreeStore()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:
    brazilian_cities = {
        'SP': ['Botucatu', 'São Manuel'],
        'SC': ['Florianópolis', 'Joinville']
    }

    def __init__(self):
        # Acessando o `Gtk.ListStore()`.
        tree_store = builder.get_object(name='tree_store')
        for state, cities_list in self.brazilian_cities.items():
            iter = tree_store.append(parent=None, row=[state])
            for city in cities_list:
                tree_store.append(parent=iter, row=[city])

    def on_row_double_click(self, widget, tree_path, tree_view_column):
        model = widget.get_model()
        print(model)
        tree_iter = model.get_iter(tree_path)
        print(tree_iter)

        column = tree_view_column.get_sort_column_id()
        print(column)
        column_title = tree_view_column.get_title()
        print(column_title)
        print(f'Coluna: {column} - Título: {column_title}')

        value = model.get_value(iter=tree_iter, column=column)
        print(f'Texto da linha {value}')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
