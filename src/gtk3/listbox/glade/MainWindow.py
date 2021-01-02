# -*- coding: utf-8 -*-
"""Gtk.ListBox()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def __init__(self):
        listbox_1 = builder.get_object(name='listbox_1')
        listbox_2 = builder.get_object(name='listbox_2')

        # Loop para criar os widgets.
        for n in range(1, 4):
            row = Gtk.ListBoxRow.new()

            hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            hbox.set_border_width(border_width=6)
            # Adicionando container na linha
            row.add(widget=hbox)

            label = Gtk.Label.new(str=f'Linha {n}')
            label.set_xalign(xalign=0)
            hbox.pack_start(child=label, expand=True, fill=True, padding=0)

            switch = Gtk.Switch.new()
            hbox.pack_start(child=switch, expand=False, fill=True, padding=0)

            listbox_1.add(widget=row)

        # Dados que serão inseridos nas linhas do listbox_2
        self.dados = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

        # Loop para criar as linhas.
        for item in self.dados:
            listbox_2.add(widget=Gtk.Label.new(str=item))

    def _on_row_clicked(self, listbox, listboxrow):
        # Exibindo qual dos itens foi clicado.
        print(f'Clicou no {self.dados[listboxrow.get_index()]}')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
