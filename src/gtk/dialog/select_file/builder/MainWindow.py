# -*- coding: utf-8 -*-
"""Dialogo para selecionar arquivo."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk

from DialogSelectFile import DialogSelectFile


@Gtk.Template(filename='./MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    check_button = Gtk.Template.Child(name='check_button')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def open_dialog(self, widget):
        select_multiple = self.check_button.get_active()
        dialog = DialogSelectFile(select_multiple=select_multiple)
        dialog.set_transient_for(parent=self)

        # Executando a janela de dialogo e aguardando uma resposta.
        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            dialog.show_file()

        # Destruindo a janela de dialogo.
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
