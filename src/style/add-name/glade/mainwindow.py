# -*- coding: utf-8 -*-
"""Aplicando estilo via propriedade `name` (Gnome Glade).

Propriedade `name` é adicionada via arquivo de interface
e arquivo css é carregado via linguagem de programação.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class Handler:
    def __init__(self):
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
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())
    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
