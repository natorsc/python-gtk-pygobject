# -*- coding: utf-8 -*-
"""Handy.HeaderBar."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Handy.HeaderBar')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        pass


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
