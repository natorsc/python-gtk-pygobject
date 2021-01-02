# -*- coding: utf-8 -*-
"""Gtk.MenuButton()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, GdkPixbuf


class Handler:
    logo = GdkPixbuf.Pixbuf.new_from_file(filename='../../../assets/icons/icon.png')

    def __init__(self):
        pass


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
