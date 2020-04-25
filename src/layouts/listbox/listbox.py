# -*- coding: utf-8 -*-
"""Contêiner do tipo ListBox layout.

O ListBox nos permite criar linhas (listas) que contenham outros
widgets dentro de si.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='ListBox Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')


        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        listbox_1 = Gtk.ListBox.new()
        # Definindo o modo de seleção.
        listbox_1.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        vbox.pack_start(child=listbox_1, expand=True, fill=True, padding=0)

        # Loop para criar os widgets.
        for n in range(1, 4):
            row = Gtk.ListBoxRow.new()
            hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            # Adicionando container na linha
            row.add(widget=hbox)

            label = Gtk.Label.new(str=f'Linha {n}')
            label.set_xalign(xalign=0)
            hbox.pack_start(child=label, expand=True, fill=True, padding=0)

            switch = Gtk.Switch.new()
            hbox.pack_start(child=switch, expand=False, fill=True, padding=0)

            listbox_1.add(widget=row)

        # Criando um segundo ListBox
        listbox_2 = Gtk.ListBox.new()
        # Definindo um sinal (evento).
        listbox_2.connect('row-activated', self._on_row_clicked)
        vbox.pack_start(child=listbox_2, expand=True, fill=True, padding=0)

        # Dados que serão inseridos nas linhas do listbox_2
        self.dados = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

        # Loop para criar as linhas.
        for item in self.dados:
            listbox_2.add(widget=Gtk.Label.new(str=item))

    def _on_row_clicked(self, listbox, listboxrow):
        # Exibindo qual dos itens foi clicado.
        print(f'Clicou no {self.dados[listboxrow.get_index()]}')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
