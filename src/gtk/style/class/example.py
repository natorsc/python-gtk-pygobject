# -*- coding: utf-8 -*-
"""Código de exemplo com 4 labels:

- 2 labels onde foi definida uma classe `label-bg-red`.
- 2 sem a propriedade name.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Código de exemplo')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} COM classe label-bg-red')
            label.get_style_context().add_class(class_name='label-bg-red')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} SEM classe label-bg-red')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
