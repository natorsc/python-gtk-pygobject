# -*- coding: utf-8 -*-
"""Handy.HeaderGroup().

Não sei implementar.
"""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.HeaderGroup')
        # self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        header_bar_1 = Handy.HeaderBar.new()
        header_bar_1.set_title(title='Handy.HeaderBar')
        header_bar_1.set_subtitle(subtitle='Handy.HeaderBar')
        header_bar_1.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=header_bar_1)

        header_bar_2 = Handy.HeaderBar.new()
        header_bar_2.set_name(name='header-bar-2')
        header_bar_2.set_title(title='Header Bar 2')
        header_bar_2.set_subtitle(subtitle='Header Bar 2')
        header_bar_2.set_show_close_button(setting=True)

        header_bar_3 = Handy.HeaderBar.new()
        header_bar_3.set_name(name='header-bar-3')
        header_bar_3.set_title(title='Header Bar 3')
        header_bar_3.set_subtitle(subtitle='Header Bar 3')
        header_bar_3.set_show_close_button(setting=True)

        button_header_bar_1 = Gtk.Button.new_with_label(label='Botão Header Bar 1')
        button_header_bar_1.connect('clicked', self.change_header_bar)
        header_bar_1.add(widget=button_header_bar_1)

        button_header_bar_2 = Gtk.Button.new_with_label(label='Botão Header Bar 2')
        button_header_bar_2.connect('clicked', self.change_header_bar)
        header_bar_2.add(widget=button_header_bar_2)

        self.hdy_header_group = Handy.HeaderGroup.new()
        self.hdy_header_group.set_decorate_all(decorate_all=True)
        self.hdy_header_group.add_header_bar(header_bar=header_bar_1)
        self.hdy_header_group.add_header_bar(header_bar=header_bar_2)
        self.hdy_header_group.add_header_bar(header_bar=header_bar_3)

        self.show_all()

    def change_header_bar(self, button):
        # self.hdy_header_group.remove_header_bar(header_bar=self.hdy_header_group.get_children()[0])

        print(self.hdy_header_group.get_children()[0])
        print(len(self.hdy_header_group.get_children()))

        for teste in self.hdy_header_group.get_children():
            print(teste.get_header_bar())
        print(dir(self.hdy_header_group.get_children()[0]))


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
