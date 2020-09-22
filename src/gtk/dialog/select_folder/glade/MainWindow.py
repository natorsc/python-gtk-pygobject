# -*- coding: utf-8 -*-
"""Dialogo para selecionar pasta."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self):

        self.check_button = builder.get_object(name='check_button')

    def open_dialog(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./DialogSelectFolder.glade')

        select_multiple = self.check_button.get_active()
        dialog = builder.get_object(name='DialogSelectFolder')
        # Definindo a janela pai.
        dialog.set_transient_for(parent=win)
        # Defininido se a seleção será multipla ou não
        dialog.set_select_multiple(select_multiple=select_multiple)
        # Pasta onde o diálogo será aberto.
        dialog.set_current_folder(filename=str(self.home))

        # É obrigatório utilizar ``show_all()``.
        dialog.show_all()

        # Executando o dialogo e recebendo a resposta.
        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            if select_multiple:
                print('Botão SALVAR pressionado')
                print('CheckBox ESTÁ marcado')
                print(f'Caminho até as pastas: {dialog.get_filenames()}')
                print(f'URI das pastas: {dialog.get_uris()}')
            else:
                print('Botão SALVAR pressionado')
                print('CheckBox NÃO está marcado')
                print(f'Caminho até a pasta: {dialog.get_filename()}')
                print(f'URI da pasta: {dialog.get_uri()}')

        dialog.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
