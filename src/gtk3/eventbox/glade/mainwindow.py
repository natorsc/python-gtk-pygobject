# -*- coding: utf-8 -*-
"""GTK.EventBox()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def __init__(self):
        pass

    def on_event_box_clicked(self, widget, event):
        print('O label foi clicado')
        print(widget)
        print(event)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
