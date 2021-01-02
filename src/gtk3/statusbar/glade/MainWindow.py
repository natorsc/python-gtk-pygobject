# -*- coding: utf-8 -*-
"""Gtk.Statusbar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    message_id = None

    def __init__(self):
        self.statusbar = builder.get_object(name='statusbar')
        self.context_id = self.statusbar.get_context_id(context_description='exemplo')

    def statusbar_show_msg(self, widget):
        self.message_id = self.statusbar.push(
            context_id=self.context_id,
            text='Texto que será exibido no statusbar.',
        )

    def statusbar_remove_msg(self, widget):
        # self.statusbar.remove(
        #     context_id=self.context_id,
        #     message_id=self.message_id,
        # )
        self.statusbar.remove_all(context_id=self.context_id)


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
