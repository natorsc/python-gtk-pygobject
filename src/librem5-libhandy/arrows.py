# -*- coding: utf-8 -*-
"""Handy.Arrows."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Handy.Arrows')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        # Handy.Arrows.
        hdy_arrow = Handy.Arrows.new()
        hdy_arrow.set_count(count=3)
        hdy_arrow.set_direction(direction=Handy.ArrowsDirection.LEFT)
        # Duração em ms (milissegundos).
        hdy_arrow.set_duration(duration=2000)
        self.add(widget=hdy_arrow)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
