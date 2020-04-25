# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./overlay.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    overlay = Gtk.Template.Child(name='overlay')

    def __init__(self):
        super().__init__()
        botao1 = Gtk.Button.new_with_label(label='Botão 1')
        botao1.set_valign(Gtk.Align.START)

        botao2 = Gtk.Button.new_with_label(label='Botão 2')
        botao2.set_valign(Gtk.Align.END)

        botao3 = Gtk.Button.new_with_label(label='Botão 3')
        botao3.set_valign(Gtk.Align.CENTER)

        self.overlay.add_overlay(widget=botao1)
        self.overlay.add_overlay(widget=botao2)
        self.overlay.add_overlay(widget=botao3)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
