# -*- coding: utf-8 -*-
"""Gtk.Fixed()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:

    def __init__(self):
        self.fixed = builder.get_object(name='fixed')

    def _on_button_clicked(self, button):
        # Quando botão é clicado o mesmo é movido para uma nova posição.
        self.fixed.move(widget=button, x=100, y=100)
        button.set_label(label='Movido')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
