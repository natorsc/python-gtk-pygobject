# -*- coding: utf-8 -*-
"""Gtk.Entry()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Entry')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        label = Gtk.Label.new(
            str='Digite algo e clique no ícone ou pressione Enter:',
        )
        vbox.pack_start(child=label, expand=False, fill=True, padding=0)

        entry = Gtk.Entry.new()
        entry.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.PRIMARY,
            icon_name='system-search-symbolic',
        )
        entry.connect('activate', self.on_key_enter_pressed)
        entry.connect('icon-press', self.on_icon_pressed)
        vbox.pack_start(child=entry, expand=False, fill=True, padding=0)

        self.show_all()

    def on_key_enter_pressed(self, widget):
        print(f'Valor digitado no entry: {widget.get_text()}')

    def on_icon_pressed(self, widget, icon, event):
        print(f'Valor digitado no entry: {widget.get_text()}')


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
