# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


@Gtk.Template(filename='./MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    overlay = Gtk.Template.Child(name='overlay')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        botao1 = Gtk.Button.new_with_label(label='Botão 1')
        botao1.set_valign(Gtk.Align.START)

        botao2 = Gtk.Button.new_with_label(label='Botão 2')
        botao2.set_valign(Gtk.Align.END)

        botao3 = Gtk.Button.new_with_label(label='Botão 3')
        botao3.set_valign(Gtk.Align.CENTER)

        self.overlay.add_overlay(widget=botao1)
        self.overlay.add_overlay(widget=botao2)
        self.overlay.add_overlay(widget=botao3)

        self.show_all()


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
