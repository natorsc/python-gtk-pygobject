# -*- coding: utf-8 -*-
"""Lendo e aplicando estilo através de um arquivo css personalizado."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    # Atibuindo as configurações do aplicativo em uma variável.
    settings = Gtk.Settings.get_default()

    def __init__(self):

        switch = builder.get_object(name='switch')
        switch.connect('notify::active', self.on_switch_clicked)

    def on_switch_clicked(self, widget, state):
        if widget.get_active():
            self.settings.set_property(
                'gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property(
                'gtk-application-prefer-dark-theme', False)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
