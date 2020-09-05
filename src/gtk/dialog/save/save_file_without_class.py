# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo vazio do tipo ``txt``.
"""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Janela de diálogo do tipo salvar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(vbox)

        button_save_file = Gtk.Button.new_with_label('Salvar arquivo')
        button_save_file.connect("clicked", self.open_dialog_save_file)
        vbox.add(button_save_file)

    def open_dialog_save_file(self, widget):
        dialog = Gtk.FileChooserDialog(parent=self)
        dialog.set_modal(modal=True)
        dialog.set_title(title='Salvar Arquivo')
        dialog.set_action(action=Gtk.FileChooserAction.SAVE)

        # Botões que serão exibidos.
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE, Gtk.ResponseType.OK
        )

        # Nome padrão do arquivo.
        dialog.set_current_name(name='novo-arquivo.txt')

        # Definindo o diretório padrão.
        home = str(Path.home())
        dialog.set_current_folder(filename=home)

        # Adicionando confirmação de sobrescrita.
        dialog.set_do_overwrite_confirmation(do_overwrite_confirmation=True)

        filter_text = Gtk.FileFilter()
        filter_text.set_name("TXT")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Todos")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

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
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
