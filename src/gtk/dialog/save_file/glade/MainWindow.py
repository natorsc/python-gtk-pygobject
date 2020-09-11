# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo do tipo ``txt`` com um texto
qualquer.
"""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self):
        pass

    def open_dialog(self, widget):
        builder = Gtk.Builder.new()
        builder.add_from_file(filename='./DialogSaveFile.glade')

        dialog = builder.get_object(name='DialogSaveFile')
        # Definindo a janela pai.
        dialog.set_transient_for(parent=win)
        # Nome inicial do arquivo.
        dialog.set_current_name(name='novo-arquivo.txt')
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

        # Executando o dialogo e recebendo a resposta.
        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            print('Botão SALVAR pressionado')
            print(f'Caminho até o arquivo: {dialog.get_filename()}')
            print(f'URI até o arquivo: {dialog.get_uri()}')
            file = dialog.get_filename()
            with open(file=file, mode='w') as f:
                text = 'Olá Mundo.'
                f.write(text)
                f.close()

        dialog.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
