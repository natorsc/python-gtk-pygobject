# -*- coding: utf-8 -*-
"""Gtk.InfoBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, GLib


class Handler:

    def __init__(self):
        self.info_bar = builder.get_object(name='info_bar')

    def on_info_bar_button_clicked(self, widget, response):
        if response == Gtk.ResponseType.CLOSE:
            self.info_bar.set_revealed(revealed=False)

    def on_button_clicked(self, widget):
        if not self.info_bar.get_revealed():
            self.info_bar.set_revealed(revealed=True)
            GLib.timeout_add_seconds(priority=0, interval=5, function=self.info_bar_timeout)

    def info_bar_timeout(self):
        self.info_bar.set_revealed(revealed=False)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
