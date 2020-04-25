# -*- coding: utf-8 -*-
"""Exemplo de ícones standard e symbolic."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='gnome_icons.glade')
class MainWindow(Gtk.ApplicationWindow):
    # Variável **DEVE** ter o mesmo nome do parâmetro
    # ``class`` do arquivo de inteface.
    __gtype_name__ = 'MainWindow'


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
