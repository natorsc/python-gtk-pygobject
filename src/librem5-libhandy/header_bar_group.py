# -*- coding: utf-8 -*-
"""Handy.HeaderGroup. Não sei implementar"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    header_bar_list = list()

    def __init__(self):
        super().__init__()

        self.set_title(title='Handy.HeaderGroup')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        header_bar_1 = Gtk.HeaderBar.new()
        header_bar_1.set_name(name='header-bar-1')
        header_bar_1.set_title(title='Header Bar 1')
        header_bar_1.set_subtitle(subtitle='Header Bar 1')
        header_bar_1.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=header_bar_1)

        header_bar_2 = Gtk.HeaderBar.new()
        header_bar_2.set_name(name='header-bar-2')
        header_bar_2.set_title(title='Header Bar 2')
        header_bar_2.set_subtitle(subtitle='Header Bar 2')
        header_bar_2.set_show_close_button(setting=True)
        # self.set_titlebar(titlebar=header_bar_2)

        button_header_bar_1 = Gtk.Button.new_with_label(label='Mudar para o Header Bar 2')
        button_header_bar_1.connect('clicked', self.change_header_bar)
        header_bar_1.add(widget=button_header_bar_1)

        button_header_bar_2 = Gtk.Button.new_with_label(label='Mudar para o Header Bar 1')
        button_header_bar_2.connect('clicked', self.change_header_bar)
        header_bar_2.add(widget=button_header_bar_2)

        self.hdy_header_group = Handy.HeaderGroup.new()
        self.hdy_header_group.add_header_bar(header_bar=header_bar_1)
        self.hdy_header_group.add_header_bar(header_bar=header_bar_2)
        self.header_bar_list.extend(self.hdy_header_group.get_header_bars())

    def change_header_bar(self, button):
        current_header_bar = button.get_parent()
        print(current_header_bar)
        header_bar_name = current_header_bar.get_name()
        print(header_bar_name)
        header_bar_list = self.hdy_header_group.get_header_bars()
        print(header_bar_list)

        print(self.header_bar_list)

        if current_header_bar.get_name() == 'header-bar-1':
            pass
        else:
            pass

if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
