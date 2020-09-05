# -*- coding: utf-8 -*-
"""Utilizando set_name()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Utilizando set_name()')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)

        label = Gtk.Label.new(str='Hello World')
        # Definindo o nome do componente.
        label.set_name(name='NomeDoComponente')
        self.add(widget=label)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
