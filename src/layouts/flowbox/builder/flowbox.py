# -*- coding: utf-8 -*-
"""Contêiner do tipo FlowBox Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./flowbox.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    flowbox = Gtk.Template.Child(name='flowbox')

    def __init__(self):
        super().__init__()

        for n in range(100):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            self.flowbox.add(button)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
