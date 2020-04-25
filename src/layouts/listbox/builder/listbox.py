# -*- coding: utf-8 -*-
"""Contêiner do tipo ListBox Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./listbox.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    listbox_1 = Gtk.Template.Child(name='listbox_1')
    listbox_2 = Gtk.Template.Child(name='listbox_2')

    def __init__(self):
        super().__init__()

        # Loop para criar os widgets.
        for n in range(1, 4):
            row = Gtk.ListBoxRow.new()
            hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            # Adicionando container na linha
            row.add(widget=hbox)

            label = Gtk.Label.new(str=f'Linha {n}')
            label.set_xalign(xalign=0)
            hbox.pack_start(child=label, expand=True, fill=True, padding=0)

            switch = Gtk.Switch.new()
            hbox.pack_end(child=switch, expand=False, fill=True, padding=0)

            self.listbox_1.add(widget=row)

        # Dados que serão inseridos nas linhas do listbox_2
        self.dados = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

        # Loop para criar as linhas.
        for item in self.dados:
            self.listbox_2.add(widget=Gtk.Label.new(str=item))

    @Gtk.Template.Callback()
    def _on_row_clicked(self, listbox, listboxrow):
        # Exibindo qual dos itens foi clicado.
        print(f'Clicou no {self.dados[listboxrow.get_index()]}')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
