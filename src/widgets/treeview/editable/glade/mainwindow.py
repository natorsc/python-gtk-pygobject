# -*- coding: utf-8 -*-
"""GTK TreeView, realizado a edição do valor na celula."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    brazilian_states = [
        (1, 'Acre'), (2, 'Alagoas'), (3, 'Amapá'), (4, 'Amazonas'),
        (5, 'Bahia'), (6, 'Ceará'), (7, 'Distrito Federal'), (8, 'Espírito Santo'),
        (9, 'Goiás'), (10, 'Maranhão'), (11, 'Mato Grosso'), (12, 'Mato Grosso do Sul'),
        (13, 'Minas Gerais'), (14, 'Pará'), (15, 'Paraíba'), (16, 'Paraná'),
        (17, 'Pernambuco'), (18, 'Piauí'), (19, 'Rio de Janeiro'),
        (20, 'Rio Grande do Norte'), (21, 'Rio Grande do Sul'), (22, 'Rondônia'),
        (23, 'Roraima'), (24, 'Santa Catarina'), (25, 'São Paulo'), (26, 'Sergipe'),
        (27, 'Tocantins'),
    ]

    def __init__(self):
        self.liststore = builder.get_object(name='liststore')

        for state in self.brazilian_states:
            self.liststore.append(row=state)

    def on_cell_edited(self, widget, row, value):
        column = widget.get_title().lower()
        if column == 'id':
            if value:
                self.liststore[row][0] = int(value)
        else:
            self.liststore[row][1] = value


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
