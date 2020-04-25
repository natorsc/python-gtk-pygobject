# -*- coding: utf-8 -*-
"""Abrindo o dialogo do tipo salvar aquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

from DialogSave import DialogSave


class Handler:
    def __init__(self):
        pass

    def _open_dialog(self, button):
        DialogSave()


if __name__ == '__main__':
    builder = Gtk.Builder.new()

    builder.add_from_file(filename='./MainWindow.glade')

    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())

    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')

    win.connect('destroy', Gtk.main_quit)

    win.show_all()

    Gtk.main()
