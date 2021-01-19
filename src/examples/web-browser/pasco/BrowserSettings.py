# -*- coding: utf-8 -*-
"""."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class BrowserSettings(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title(title='Configurações')
        self.set_default_size(width=1366 / 2, height=768 / 2)

        scrolled = Gtk.ScrolledWindow.new(hadjustment=None, vadjustment=None)
        self.add(widget=scrolled)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        scrolled.add(widget=vbox)

        label_start_page = Gtk.Label.new(str='Página inicial')
        label_start_page.set_xalign(xalign=0)
        vbox.pack_start(
            child=label_start_page,
            expand=False,
            fill=False,
            padding=0,
        )

        entry_start_page = Gtk.Entry.new()
        vbox.pack_start(
            child=entry_start_page,
            expand=False,
            fill=True,
            padding=0,
        )

        separetor_start_page = Gtk.Separator.new(
            orientation=Gtk.Orientation.HORIZONTAL,
        )
        vbox.pack_start(
            child=separetor_start_page,
            expand=False,
            fill=True,
            padding=6,
        )

        self.show_all()
