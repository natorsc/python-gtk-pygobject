# -*- coding: utf-8 -*-
"""Contêiner do tipo Fixed Layout."""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='./MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    fixed = Gtk.Template.Child(name='fixed')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def _on_button_clicked(self, button):
        # Quando botão é clicado o mesmo é movido para uma nova posição.
        self.fixed.move(widget=button, x=100, y=100)
        button.set_label(label='Movido')


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
