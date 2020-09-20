# -*- coding: utf-8 -*-
"""Contêiner do tipo Fixed Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self):
        super().__init__()

        self.set_title(title='Fixed Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        self.fixed = Gtk.Fixed.new()
        self.fixed.set_border_width(border_width=12)
        self.add(widget=self.fixed)

        button = Gtk.Button.new_with_label(label='Clique Aqui')
        # Adicionando uma ação para quando o botão for clicado.
        button.connect('clicked', self._on_button_clicked)
        # Posicionando o botão no Fixed Layout.
        self.fixed.put(widget=button, x=0, y=0)

    def _on_button_clicked(self, widget):
        # Quando botão é clicado o mesmo é movido para uma nova posição.
        self.fixed.move(widget=widget, x=100, y=100)
        widget.set_label(label='Movido')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
