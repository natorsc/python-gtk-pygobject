# -*- coding: utf-8 -*-
"""Dialogo para abrir arquivos."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def _set_filter(dialog):
    """Adicionando filtros ao dialogo.

    Filtro limitam os arquivos que estão sendo exibidos.
    """
    filter_python = Gtk.FileFilter()
    filter_python.set_name("Python")
    filter_python.add_mime_type("text/x-python")
    dialog.add_filter(filter=filter_python)

    filter_text = Gtk.FileFilter()
    filter_text.set_name("TXT")
    filter_text.add_mime_type("text/plain")
    dialog.add_filter(filter=filter_text)

    filter_any = Gtk.FileFilter()
    filter_any.set_name("Todos")
    filter_any.add_pattern("*")
    dialog.add_filter(filter=filter_any)


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Dialogo para abrir arquivos')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        button_open_file = Gtk.Button.new_with_label(label='Abrir arquivo')
        button_open_file.connect("clicked", self.open_select_file)
        vbox.add(widget=button_open_file)

        self.check_button = Gtk.CheckButton.new_with_label(label='Selecionar multiplos arquivos?')
        vbox.add(widget=self.check_button)

    def open_select_file(self, button):
        dialog = Gtk.FileChooserDialog(
            name='selecionar-arquivo',
            title='Selecionar Arquivo',
            parent=self,
            modal=True,
            action=Gtk.FileChooserAction.OPEN,
        )
        # Adicionando os botões que serão exibidos
        dialog.add_buttons(
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL
        )
        # Adicionado filtro ao dialogo.
        _set_filter(dialog=dialog)

        # Definindo o diretório padrão.
        home = str(Path.home())
        dialog.set_current_folder(filename=home)

        if self.check_button.get_active() is True:
            dialog.set_select_multiple(select_multiple=True)

            # Executando o dialogo e recebendo a resposta.
            response = dialog.run()

            if response == Gtk.ResponseType.OK:
                print('Botão ABRIR pressionado')
                print(f'Caminho até o arquivo: {dialog.get_filenames()}')
                print(f'URI até o arquivo: {dialog.get_uris()}')

                files = dialog.get_filenames()
                for file in files:
                    with open(file=file, mode='r') as f:
                        file_content = f.read()
                        print(f'Conteúdo do arquivo:\n{file_content}')
                    f.close()
        else:
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print('Botão ABRIR pressionado')
                print(f'Caminho até o arquivo: {dialog.get_filename()}')
                print(f'URI até o arquivo: {dialog.get_uri()}')
                file = dialog.get_filename()
                with open(file=file, mode='r') as f:
                    file_content = f.read()
                    print(f'\nConteúdo do arquivo:\n{file_content}')
                    f.close()

        dialog.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
