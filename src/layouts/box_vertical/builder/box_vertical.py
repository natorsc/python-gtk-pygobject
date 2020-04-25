# -*- coding: utf-8 -*-
"""Box layout vertical."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='box_vertical.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
