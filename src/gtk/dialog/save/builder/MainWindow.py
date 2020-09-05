# -*- coding: utf-8 -*-
"""Abrindo o dialogo do tipo salvar aquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

from DialogSave import DialogSave


# Parâmetros aceitos: @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='./MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    @Gtk.Template.Callback()
    def _open_dialog(self, button):
        DialogSave(parent=self)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
