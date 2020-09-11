# -*- coding: utf-8 -*-
"""Dialogo para selecionar arquivo."""
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
        builder.add_from_file(filename='./DialogSelectFile.glade')

        select_multiple = self.check_button.get_active()
        dialog = builder.get_object(name='DialogSelectFile')
        # Definindo a janela pai.
        dialog.set_transient_for(parent=win)
        # Defininido se a seleção será multipla ou não
        dialog.set_select_multiple(select_multiple=select_multiple)
        # Pasta onde o diálogo será aberto.
        dialog.set_current_folder(filename=str(self.home))

        # Criando e adicionando filtros.
        txt_filter = Gtk.FileFilter()
        txt_filter.set_name(name='txt')
        txt_filter.add_pattern(pattern='.txt')
        txt_filter.add_mime_type(mime_type='text/plain')
        dialog.add_filter(filter=txt_filter)

        py_filter = Gtk.FileFilter()
        py_filter.set_name(name='python')
        py_filter.add_pattern(pattern='.py')
        py_filter.add_mime_type(mime_type='text/x-python')
        dialog.add_filter(filter=py_filter)

        all_filter = Gtk.FileFilter()
        all_filter.set_name(name='todos')
        all_filter.add_pattern(pattern='*')
        dialog.add_filter(filter=all_filter)

        # É obrigatório utilizar ``show_all()``.
        dialog.show_all()

        # Executando o dialogo e recebendo a resposta.
        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            if select_multiple:
                print('Botão SALVAR pressionado')
                print('CheckBox ESTÁ marcado')
                print(f'Caminho até os arquivos: {dialog.get_filenames()}')
                print(f'URI dos arquivos: {dialog.get_uris()}')
            else:
                print('Botão SALVAR pressionado')
                print('CheckBox NÃO está marcado')
                print(f'Caminho até o arquivo: {dialog.get_filename()}')
                print(f'URI do arquivo: {dialog.get_uri()}')

        dialog.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
