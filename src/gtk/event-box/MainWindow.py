# -*- coding: utf-8 -*-
"""Gtk.EventBox()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.EventBox')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(widget=vbox)

        hdy_window_handle = Gtk.EventBox.new()
        hdy_window_handle.connect('button-press-event', self.on_event_box_clicked)
        vbox.pack_start(child=hdy_window_handle, expand=True, fill=True, padding=0)

        label = Gtk.Label.new(str='Clique no label')
        hdy_window_handle.add(widget=label)

        self.show_all()

    def on_event_box_clicked(self, widget, event):
        print('O label foi clicado')
        print(widget)
        print(event)


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
