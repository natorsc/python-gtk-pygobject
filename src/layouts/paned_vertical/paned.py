# -*- coding: utf-8 -*-
"""Contêiner do tipo Paned Layout.

Neste gerenciador de layout temos a criação de 2 frames (painéis) onde
são posicionados os widgets.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Paned Layout Vertical')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        paned = Gtk.Paned().new(Gtk.Orientation.VERTICAL)
        paned.set_border_width(border_width=12)
        self.add(widget=paned)

        vbox1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        paned.pack1(child=vbox1, resize=False, shrink=False)

        vbox2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        paned.pack2(child=vbox2, resize=False, shrink=False)

        # vbox1
        for n in range(1, 6):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            vbox1.add(widget=button)

        # vbox2
        for n in range(6, 11):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            vbox2.add(widget=button)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
