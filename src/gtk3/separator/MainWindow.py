# -*- coding: utf-8 -*-
"""Gtk.Separator()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Separator')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_border_width(border_width=12)
        self.add(widget=hbox)

        vbox_left = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        hbox.pack_start(child=vbox_left, expand=False, fill=True, padding=0)

        separator = Gtk.Separator.new(
            orientation=Gtk.Orientation.VERTICAL,
        )
        hbox.pack_start(child=separator, expand=False, fill=True, padding=6)

        vbox_right = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        hbox.pack_start(child=vbox_right, expand=False, fill=True, padding=0)

        for i in range(2):
            button = Gtk.Button.new_with_label(label=f'Botão {i}')
            vbox_left.pack_start(child=button, expand=False, fill=True, padding=0)

            hseparator = Gtk.Separator.new(
                orientation=Gtk.Orientation.HORIZONTAL,
            )
            vbox_left.pack_start(
                child=hseparator,
                expand=False,
                fill=True,
                padding=12,
            )

            label = Gtk.Label.new(str=f'Lorem Ipsum is simply dummy text of the '
                                      f'printing and typesetting industry ({i})')
            vbox_right.pack_start(child=label, expand=True, fill=True, padding=0)

            vseparator = Gtk.Separator.new(
                orientation=Gtk.Orientation.VERTICAL,
            )
            vbox_right.pack_start(
                child=vseparator,
                expand=False,
                fill=True,
                padding=6,
            )

        self.show_all()


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
