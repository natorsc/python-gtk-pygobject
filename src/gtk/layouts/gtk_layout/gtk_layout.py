# -*- coding: utf-8 -*-
"""Contêiner do tipo Gtk Layout.

``Gtk.Layout`` é similar ao ``Gtk.DrawingArea``, contudo ``Gtk.Layout``
é apenas um espaço em branco.

De preferencia por ``Gtk.DrawingArea`` ou ``Gtk.Fixed``.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Gtk Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')
        self.set_border_width(border_width=12)

        layout = Gtk.Layout.new()
        self.add(widget=layout)

        x = 0
        y = 0
        for n in range(1, 7):
            # Criando widget do tipo botão e definindo um label (nome).
            button = Gtk.Button.new_with_label(label=f'Botão {n}')

            # Com base nos eixos x e y.
            layout.put(child_widget=button, x=x, y=y)
            x += 50
            y += 50


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
