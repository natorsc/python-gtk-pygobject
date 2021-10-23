# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.FileChooserDialog() salvar arquivo."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class DialogSelecFolder(Gtk.FileChooserDialog):
    # Definindo o diretório padrão.
    HOME = str(Path.home())

    def __init__(self, parent):
        super().__init__(transient_for=parent, use_header_bar=True)

        self.set_action(action=Gtk.FileChooserAction.SAVE)
        self.set_title(title='Salvar arquivo')
        self.set_modal(modal=True)
        # Nome inicial do arquivo.
        self.set_current_name(name='novo-arquivo.txt')
        self.connect('response', self.dialog_response)
        self.set_current_folder(
            Gio.File.new_for_path(self.HOME),
        )
        # Adicionando confirmação de sobrescrita.
        # self.set_do_overwrite_confirmation(do_overwrite_confirmation=True)

        # Criando os botões que ficarão na barra de título (Gtk.HeaderBar()).
        self.add_buttons(
            '_Cancelar', Gtk.ResponseType.CANCEL,
            '_Selecionar', Gtk.ResponseType.OK
        )
        btn_select = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        # Adicionando estilo no botão.
        btn_select.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        self.show()

    def dialog_response(self, widget, response):
        # Verificando qual botão foi pressionado.
        if response == Gtk.ResponseType.OK:
            glocalfile = self.get_file()
            print(f'Nome do arquivo selecionada: {glocalfile.get_basename()}')
            print(f'Caminho onde o arquivo será salvo: {glocalfile.get_path()}')

            file_path = glocalfile.get_path()
            self.save_file(file_path=file_path)

        widget.close()

    def save_file(self, file_path):
        with open(file=file_path, mode='w') as f:
            f.write('Olá Mundo')
            f.close()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.FileChooserDialog() abrir arquivo')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        button_save_file = Gtk.Button.new_with_label(label='Salvar arquivo')
        button_save_file.connect('clicked', self.open_dialog)
        vbox.append(child=button_save_file)

    def open_dialog(self, widget):
        DialogSelecFolder(parent=self)


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
    import sys

    app = Application()
    app.run(sys.argv)
