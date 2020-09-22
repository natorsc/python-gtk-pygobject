# -*- coding: utf-8 -*-
"""Contêiner do tipo Overlay Layout"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

    def __init__(self):
        overlay = builder.get_object(name='overlay')

        botao1 = Gtk.Button.new_with_label(label='Botão 1')
        botao1.set_valign(Gtk.Align.START)

        botao2 = Gtk.Button.new_with_label(label='Botão 2')
        botao2.set_valign(Gtk.Align.END)

        botao3 = Gtk.Button.new_with_label(label='Botão 3')
        botao3.set_valign(Gtk.Align.CENTER)

        overlay.add_overlay(widget=botao1)
        overlay.add_overlay(widget=botao2)
        overlay.add_overlay(widget=botao3)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
