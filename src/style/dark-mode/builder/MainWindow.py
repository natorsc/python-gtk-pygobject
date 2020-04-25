# -*- coding: utf-8 -*-
"""Ativando e desativando o modo escuro do GTK em um arquivo de
interface do Gnome Builder."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


# Parâmetros aceitos: @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='mainwindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    # Variável **DEVE** ter o mesmo nome do parâmetro
    # ``class`` do arquivo de inteface.
    __gtype_name__ = 'MainWindow'

    # Atibuindo as configurações do aplicativo em uma variável.
    settings = Gtk.Settings.get_default()

    @Gtk.Template.Callback()
    def on_switch_clicked(self, widget, state):
        if widget.get_active():
            self.settings.set_property('gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property('gtk-application-prefer-dark-theme', False)


if __name__ == '__main__':
    win = MainWindow()
    win.set_position(position=Gtk.WindowPosition.CENTER)
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
