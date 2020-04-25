# -*- coding: utf-8 -*-
"""Ativando e desativando o modo escuro do GTK em um arquivo de
interface do Gnome Glade.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    settings = Gtk.Settings.get_default()

    def on_switch_clicked(self, widget, state):
        if widget.get_active():
            self.settings.set_property('gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property('gtk-application-prefer-dark-theme', False)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.set_position(position=Gtk.WindowPosition.CENTER)
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
