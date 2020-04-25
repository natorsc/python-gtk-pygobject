# -*- coding: utf-8 -*-
"""Adicionando classe via Gnome builder.

Classe é adicionada via arquivo de interface e o
arquivo css é carregado via linguagem de programação.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gdk


@Gtk.Template(filename='./mainwindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self):
        super().__init__()
        self._set_custom_css(file='../css/custom.css')

    @staticmethod
    def _set_custom_css(file):
        css_provider = Gtk.CssProvider.new()
        css_provider.load_from_path(path=file)

        screen = Gdk.Screen()

        style_context = Gtk.StyleContext.new()
        style_context.add_provider_for_screen(
            screen=screen.get_default(),
            provider=css_provider,
            priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
