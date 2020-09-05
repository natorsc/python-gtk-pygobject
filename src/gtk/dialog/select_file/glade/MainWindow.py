# -*- coding: utf-8 -*-
"""Abrindo o dialogo do tipo abrir aquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

from DialogOpenFile import DialogOpenFile


class Handler:
    def __init__(self, widgets):
        self.check_button = widgets.get_object(name='check_button')

    def _open_dialog(self, button):
        check_button_status = self.check_button.get_active()
        DialogOpenFile(select_multiple=check_button_status)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())
    builder.connect_signals(obj_or_map=Handler(widgets=builder))
    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
