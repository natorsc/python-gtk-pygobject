# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Overlay Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')
        self.set_border_width(border_width=12)

        botao1 = Gtk.Button.new_with_label(label='Botão 1')
        botao1.set_valign(Gtk.Align.START)

        botao2 = Gtk.Button.new_with_label(label='Botão 2')
        botao2.set_valign(Gtk.Align.END)

        botao3 = Gtk.Button.new_with_label(label='Botão 3')
        botao3.set_valign(Gtk.Align.CENTER)

        overlay = Gtk.Overlay.new()

        overlay.add_overlay(widget=botao1)
        overlay.add_overlay(widget=botao2)
        overlay.add_overlay(widget=botao3)
        self.add(widget=overlay)

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
