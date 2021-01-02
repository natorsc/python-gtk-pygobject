# -*- coding: utf-8 -*-
"""Gtk.TreeView(), Gtk.TreeStore()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gio


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    brazilian_cities = {
        'SP': ['Botucatu', 'São Manuel'],
        'SC': ['Florianópolis', 'Joinville']
    }

    tree_store = Gtk.Template.Child(name='tree_store')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for state, cities_list in self.brazilian_cities.items():
            iter = self.tree_store.append(parent=None, row=[state])
            for city in cities_list:
                self.tree_store.append(parent=iter, row=[city])

    @Gtk.Template.Callback()
    def on_row_double_click(self, widget, tree_path, tree_view_column):
        model = widget.get_model()
        tree_iter = model.get_iter(tree_path)

        column = tree_view_column.get_sort_column_id()
        column_title = tree_view_column.get_title()
        print(f'Coluna: {column} - Título: {column_title}')

        value = model.get_value(iter=tree_iter, column=column)
        print(f'Texto da linha {value}')


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
