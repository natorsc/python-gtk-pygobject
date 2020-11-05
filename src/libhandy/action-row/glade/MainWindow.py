# -*- coding: utf-8 -*-
"""Handy.ActionRow()."""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk
from gi.repository import Handy


class Handler:
    # Nome dos ícones.
    icons_standard = ['mail-send-receive', 'user-trash', 'face-smile',
                      'call-start', 'call-stop']

    def __init__(self):
        # Acessar os widgets da interface com builder.get_object(name) aqui:
        list_box = builder.get_object(name='list_box')

        for n in range(len(self.icons_standard)):
            # Criando e configurando ActionRow que será adicionada no listbox.
            hdy_action_row = Handy.ActionRow.new()
            hdy_action_row.set_icon_name(icon_name=self.icons_standard[n - 1])
            hdy_action_row.set_title(title=f'Título {n}')
            hdy_action_row.set_subtitle(subtitle=f'subtítulo {n}')
            # Adicionando a ActionRow no listbox.
            list_box.add(widget=hdy_action_row)

    def on_row_clicked(self, listbox, row):
        # Exibindo qual dos itens foi clicado.
        print(f'Ícone da linha = {row.get_icon_name()}')
        print(f'Titulo da linha = {row.get_title()}')
        print(f'Sub titulo da linha = {row.get_subtitle()}')
        print(f'Posição = {row.get_index()}')
        print('---\n')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
