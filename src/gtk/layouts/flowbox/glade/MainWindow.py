# -*- coding: utf-8 -*-
"""Contêiner do tipo FlowBox Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def __init__(self):
        flowbox = builder.get_object(name='flowbox')

        for n in range(100):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            flowbox.add(button)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
