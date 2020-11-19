# -*- coding: utf-8 -*-
"""Gtk.Calendar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Calendar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        calendar = Gtk.Calendar.new()
        calendar.connect('day-selected-double-click', self.day_double_click)
        vbox.pack_start(child=calendar, expand=True, fill=True, padding=0)

        self.show_all()

    def day_double_click(self, widget):
        date = widget.get_date()
        print(f'Dia: {date.day}')
        print(f'Mês: {date.month}')
        print(f'Ano: {date.year}')


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
