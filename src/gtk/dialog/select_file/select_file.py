# -*- coding: utf-8 -*-
"""Dialogo para abrir arquivos."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class DialogSelectFile(Gtk.FileChooserDialog):
    def __init__(self, parent, select_multiple):
        """Construtor.

        :param parent: Widget ao qual o dialogo pertence.
        """
        super().__init__(parent=parent, select_multiple=select_multiple)

        self.set_title(title='Selecionar Arquivo(s)')
        self.set_modal(modal=True)
        self.set_action(action=Gtk.FileChooserAction.OPEN)

        # Adicionado filtro ao dialogo.
        self._set_filter()

        # Definindo o diretório padrão.
        home = str(Path.home())
        self.set_current_folder(filename=home)

        # Botões que serão exibidos.
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK
        )

        self.show_all()

    def _set_filter(self):
        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python")
        filter_py.add_mime_type("text/x-python")
        self.add_filter(filter=filter_py)

        filter_text = Gtk.FileFilter()
        filter_text.set_name("TXT")
        filter_text.add_mime_type("text/plain")
        self.add_filter(filter=filter_text)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Todos")
        filter_any.add_pattern("*")
        self.add_filter(filter=filter_any)


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Dialogo para abrir arquivos')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        button_open_file = Gtk.Button.new_with_label('Abrir arquivo')
        button_open_file.connect("clicked", self.open_select_file)
        vbox.add(widget=button_open_file)

        self.check_button = Gtk.CheckButton.new_with_label(label='Selecionar multiplos arquivos?')
        vbox.add(widget=self.check_button)

    def open_select_file(self, button):
        check_button_status = self.check_button.get_active()
        dialog = DialogSelectFile(parent=self, select_multiple=check_button_status)

        if check_button_status is True:
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print(f'Caminho até o arquivo: {dialog.get_filenames()}')
                print(f'URI até o arquivo: {dialog.get_uris()}')

                files = dialog.get_filenames()
                for file in files:
                    with open(file=file, mode='r') as f:
                        file_content = f.read()
                        print(f'Conteúdo do arquivo: \n{file_content}')
                    f.close()
        else:
            # Executando o dialogo e recebendo a resposta.
            response = dialog.run()

            # Verificando a resposta recebida.
            if response == Gtk.ResponseType.OK:
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
