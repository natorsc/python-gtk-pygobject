# -*- coding: utf-8 -*-
"""Gtk.RadioButton()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:

    def on_radiobutton_toggled(self, widget):
        if widget.get_active():
            print(f'Radio button {widget.get_label()} MARCADO')
        else:
            print(f'Radio button {widget.get_label()} DESMARCADO')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
