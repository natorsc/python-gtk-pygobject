# -*- coding: utf-8 -*-
"""Lendo arquivo de interface gerado pelo Builder.

Arquivo está com a extensão glade porque o PyCharm não
abre a extensão `*.ui`.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    # Variável **DEVE** ter o mesmo nome do parâmetro
    # ``class`` do arquivo de inteface.
    __gtype_name__ = 'MainWindow'


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
