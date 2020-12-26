# -*- coding: utf-8 -*-
"""Gtk.InfoBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio, GLib


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.InfoBar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Layout
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        # Widgets.
        self.info_bar = Gtk.InfoBar.new()
        self.info_bar.set_revealed(revealed=False)
        self.info_bar.set_show_close_button(setting=True)
        self.info_bar.connect('response', self.on_info_bar_button_clicked)
        vbox.pack_start(child=self.info_bar, expand=False, fill=True, padding=0)

        message_label = Gtk.Label.new('Gtk.InfoBar clique em fechar ou aguarde 5 segundos')
        content_area = self.info_bar.get_content_area()
        content_area.add(widget=message_label)

        button = Gtk.Button.new_with_label(label='Abrir Gtk.InfoBar')
        button.connect('clicked', self.on_button_clicked)
        vbox.pack_end(child=button, expand=False, fill=True, padding=0)

        self.show_all()

    def on_info_bar_button_clicked(self, widget, response):
        if response == Gtk.ResponseType.CLOSE:
            self.info_bar.set_revealed(revealed=False)

    def on_button_clicked(self, widget):
        if not self.info_bar.get_revealed():
            self.info_bar.set_revealed(revealed=True)
            GLib.timeout_add_seconds(priority=0, interval=5, function=self.info_bar_timeout)

    def info_bar_timeout(self):
        self.info_bar.set_revealed(revealed=False)


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
