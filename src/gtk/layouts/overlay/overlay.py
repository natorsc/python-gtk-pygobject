# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Overlay Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')
        self.set_border_width(border_width=12)

        botao1 = Gtk.Button.new_with_label(label='Botão 1')
        botao1.set_valign(Gtk.Align.START)

        botao2 = Gtk.Button.new_with_label(label='Botão 2')
        botao2.set_valign(Gtk.Align.END)

        botao3 = Gtk.Button.new_with_label(label='Botão 3')
        botao3.set_valign(Gtk.Align.CENTER)

        overlay = Gtk.Overlay.new()
        overlay.add_overlay(widget=botao1)
        overlay.add_overlay(widget=botao2)
        overlay.add_overlay(widget=botao3)
        self.add(widget=overlay)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
