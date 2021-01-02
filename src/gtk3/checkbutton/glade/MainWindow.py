# -*- coding: utf-8 -*-
"""Gtk.CheckButton()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def __init__(self):
        # Acessar os widgets da interface com builder.get_object(name) aqui:
        # ...
        pass

    def on_check_button_toggled(self, widget):
        if widget.get_active():
            print('Botão marcado')
        else:
            print('Botão desmarcado')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
