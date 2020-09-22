# -*- coding: utf-8 -*-
"""Contêiner do tipo Headerbar Layout."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


@Gtk.Template(filename='./MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def _send_mail(self, button):
        print('Você clicou no botão que tem o icone de enviar/receber email')

    @Gtk.Template.Callback()
    def _left_arrow(self, button):
        print('Você clicou no botão que tem uma seta para a esquerda')

    @Gtk.Template.Callback()
    def _right_arrow(self, button):
        print('Você clicou no botão que tem uma seta para a direita')


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
