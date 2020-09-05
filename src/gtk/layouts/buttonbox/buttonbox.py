# -*- coding: utf-8 -*-
"""Contêiner do tipo ButtonBox Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        # Configurando a janela principal.
        self.set_title(title='ButtonBox Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../../images/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        button1 = Gtk.Button.new_with_label(label='Botão 1')
        button2 = Gtk.Button.new_with_label(label='Botão 2')
        button3 = Gtk.Button.new_with_label(label='Botão 3')
        button4 = Gtk.Button.new_with_label(label='Botão 4')
        button5 = Gtk.Button.new_with_label(label='Botão 5')
        button6 = Gtk.Button.new_with_label(label='Botão 6')

        hbuttonbox = Gtk.ButtonBox.new(orientation=Gtk.Orientation.HORIZONTAL)
        hbuttonbox.pack_start(
            child=button1, expand=False, fill=False, padding=0
        )
        hbuttonbox.pack_start(
            child=button2, expand=False, fill=False, padding=0
        )
        vbox.add(widget=hbuttonbox)

        hbuttonbox1 = Gtk.ButtonBox.new(orientation=Gtk.Orientation.HORIZONTAL)
        hbuttonbox1.set_layout(Gtk.ButtonBoxStyle.EXPAND)
        hbuttonbox1.pack_start(
            child=button3, expand=False, fill=False, padding=0
        )
        hbuttonbox1.pack_start(
            child=button4, expand=False, fill=False, padding=0
        )
        vbox.add(widget=hbuttonbox1)

        vbuttonbox = Gtk.ButtonBox.new(orientation=Gtk.Orientation.VERTICAL)
        vbuttonbox.pack_start(
            child=button5, expand=False, fill=False, padding=0
        )
        vbuttonbox.pack_start(
            child=button6, expand=False, fill=False, padding=0
        )
        vbox.add(widget=vbuttonbox)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
