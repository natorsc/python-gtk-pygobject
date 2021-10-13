# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.FileChooserDialog() selecionar pasta."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class DialogSelecFolder(Gtk.FileChooserDialog):
    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self, parent, select_multiple):
        super().__init__(transient_for=parent, use_header_bar=True)
        self.select_multiple = select_multiple

        self.set_action(action=Gtk.FileChooserAction.SELECT_FOLDER)
        self.set_title(title='Selecione uma pasta.')
        self.set_modal(modal=True)
        self.set_select_multiple(select_multiple=self.select_multiple)
        self.connect('response', self.dialog_response)
        self.set_current_folder(
            Gio.File.new_for_path(path=str(self.home)),
        )

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
            if self.select_multiple:
                gliststore = self.get_files()
                for glocalfile in gliststore:
                    print(f'Nome da pasta selecionada: {glocalfile.get_basename()}')
                    print(f'Caminho da pasta selecionada: {glocalfile.get_path()}\n')
            else:
                glocalfile = self.get_file()
                print(f'Nome da pasta selecionada: {glocalfile.get_basename()}')
                print(f'Caminho da pasta selecionada: {glocalfile.get_path()}')

        widget.close()


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.FileChooserDialog() selecionar pasta')
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

        button_save_file = Gtk.Button.new_with_label(label='Selecionar pasta')
        button_save_file.connect('clicked', self.open_dialog)
        vbox.append(child=button_save_file)

        self.check_button = Gtk.CheckButton.new_with_label(label='Selecionar várias pastas?')
        vbox.append(child=self.check_button)

    def open_dialog(self, widget):
        select_multiple = self.check_button.get_active()
        DialogSelecFolder(parent=self, select_multiple=select_multiple)


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
