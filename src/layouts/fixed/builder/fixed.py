# -*- coding: utf-8 -*-
"""Contêiner do tipo Fixed Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='./fixed.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    fixed = Gtk.Template.Child(name='fixed')

    @Gtk.Template.Callback()
    def _on_button_clicked(self, button):
        # Quando botão é clicado o mesmo é movido para uma nova posição.
        self.fixed.move(widget=button, x=100, y=100)
        button.set_label(label='Movido')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
