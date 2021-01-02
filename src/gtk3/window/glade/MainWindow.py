# -*- coding: utf-8 -*-
"""Gtk.Window()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:

    def __init__(self):
        pass

    def on_button_clicked(self, widget):
        window = Gtk.Window.new(type=Gtk.WindowType.TOPLEVEL)
        window.set_transient_for(parent=win)
        window.set_modal(modal=True)
        window.set_title(title='Gtk.Window')
        window.set_default_size(width=1366 / 3, height=768 / 3)
        window.set_default_icon_from_file(filename='../../../assets/icons/person.png')
        window.show_all()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
