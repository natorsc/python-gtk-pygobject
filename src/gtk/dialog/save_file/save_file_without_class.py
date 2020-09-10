# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo do tipo ``txt`` com um texto
qualquer.
"""
import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Janela de diálogo do tipo salvar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(vbox)

        button_save_file = Gtk.Button.new_with_label('Salvar arquivo')
        button_save_file.connect('clicked', self.open_dialog)
        vbox.add(button_save_file)

        self.show_all()

    def open_dialog(self, widget):
        dialog = Gtk.FileChooserDialog(parent=self)
        dialog.set_title(title='Salvar Arquivo')
        dialog.set_modal(modal=True)
        # Tipo de ação que o dialogo irá executar.
        dialog.set_action(action=Gtk.FileChooserAction.SAVE)
        # Nome inicial do arquivo.
        dialog.set_current_name(name='novo-arquivo.txt')
        # Pasta onde o diálogo será aberto.
        dialog.set_current_folder(filename=str(self.home))
        # Adicionando confirmação de sobrescrita.
        dialog.set_do_overwrite_confirmation(do_overwrite_confirmation=True)

        # Botões que serão exibidos.
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE, Gtk.ResponseType.OK
        )

        # Adicionando class action nos botões.
        btn_cancel = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        btn_save = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        btn_save.get_style_context().add_class(class_name='suggested-action')

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


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)
