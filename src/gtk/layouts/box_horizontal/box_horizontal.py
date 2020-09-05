# -*- coding: utf-8 -*-
"""Contêiner do tipo Box Layout horizontal.

Neste gerenciador de layout os widgets são posicionados horizontalmente.

O posicionamento pode ser:

- Da esquerda para a direita ``pack_start()``.
- Da direita para a esquerda ``pack_end()``.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Box Layout Horizontal')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')
        self.set_border_width(border_width=12)

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.add(widget=hbox)

        # Loop de repetição para criar os widgets.
        for n in range(1, 4):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            hbox.pack_start(child=button, expand=True, fill=True, padding=0)

        for n in range(1, 4):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            # Adicionando widgets da direita para a esquerda.
            hbox.pack_end(child=button, expand=True, fill=True, padding=0)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
