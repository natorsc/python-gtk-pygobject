# -*- coding: utf-8 -*-
"""Abrindo o dialogo do tipo abrir aquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk

from DialogOpenFile import DialogOpenFile


@Gtk.Template(filename='./MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    check_button = Gtk.Template.Child(name='check_button')

    @Gtk.Template.Callback()
    def _open_dialog(self, button):
        check_button_status = self.check_button.get_active()
        DialogOpenFile(select_multiple=check_button_status)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
