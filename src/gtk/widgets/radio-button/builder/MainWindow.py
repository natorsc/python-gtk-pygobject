# -*- coding: utf-8 -*-
"""GTK EntryCompletion, auto completar ao digitar."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    @Gtk.Template.Callback()
    def on_radiobutton_toggled(self, widget):
        if widget.get_active():
            print(f'Radio button {widget.get_label()} MARCADO')
        else:
            print(f'Radio button {widget.get_label()} DESMARCADO')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
