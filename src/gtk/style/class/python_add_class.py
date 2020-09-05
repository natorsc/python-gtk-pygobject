# -*- coding: utf-8 -*-
"""Utilizando get_style_context() e add_class()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Utilizando get_style_context() e add_class()')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)

        label = Gtk.Label.new(str='Hello World')
        # Definindo uma classe para o componente.
        label.get_style_context().add_class(class_name='NomeDaClasse')
        self.add(widget=label)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
