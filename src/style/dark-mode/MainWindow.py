# -*- coding: utf-8 -*-
"""Ativando e desativando o modo escuro do GTK."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Utilizando modo escuro')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=12)

        # Atibuindo as configurações do aplicativo em uma variável.
        self.settings = Gtk.Settings.get_default()

        # Widgets
        grid_layout = grid = Gtk.Grid.new()
        grid.set_column_spacing(spacing=12)
        self.add(widget=grid_layout)

        label = Gtk.Label.new(
            str='Clique no switch para ativar ou desativar o modo escuro '
                '(Dark Mode)',
        )
        grid_layout.add(widget=label)

        switch = Gtk.Switch.new()
        switch.connect('notify::active', self.on_switch_clicked)
        grid_layout.add(widget=switch)

    def on_switch_clicked(self, widget, state):
        if widget.get_active():
            self.settings.set_property('gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property('gtk-application-prefer-dark-theme', False)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
