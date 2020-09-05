# -*- coding: utf-8 -*-
"""Lendo o arquivo css e o estilo sendo aplicado."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        # Fazendo a leitura do arquivo css.
        self._set_custom_css(file='custom.css')

        self.set_title(title='Lendo o arquivo css e o estilo sendo aplicado')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} COM propriedade name')
            label.set_name(name='label-bg-red')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} SEM propriedade name')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)

    @staticmethod
    def _set_custom_css(file):
        css_provider = Gtk.CssProvider.new()
        css_provider.load_from_path(path=file)

        screen = Gdk.Screen()

        style_context = Gtk.StyleContext.new()
        style_context.add_provider_for_screen(
            screen=screen.get_default(),
            provider=css_provider,
            priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
