# -*- coding: utf-8 -*-
"""Handy.Column."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        # Configurando a janela principal.
        self.set_title(title='Handy.Column')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        hdy_column = Handy.Column.new()
        # hdy_column.set_linear_growth_width(linear_growth_width=200)
        hdy_column.set_maximum_width(maximum_width=200)
        self.add(widget=hdy_column)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hdy_column.add(widget=vbox)

        hdy_arrow = Handy.Arrows.new()
        hdy_arrow.set_count(count=5)
        hdy_arrow.set_duration(duration=2000)
        vbox.pack_start(child=hdy_arrow, expand=True, fill=False, padding=0)

        button_1 = Gtk.Button.new_with_label(label='Botão 1')
        # Adicionando widgets de cima para baixo.
        vbox.add(widget=button_1)

        button_2 = Gtk.Button.new_with_label(label='Botão 2')
        # Adicionando widgets de cima para baixo.
        vbox.add(widget=button_2)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
