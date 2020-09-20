# -*- coding: utf-8 -*-
"""Janela de diálogo personalizado com Gnome Builder."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./CustomDialog.ui')
class CustomDialog(Gtk.Dialog):
    __gtype_name__ = 'CustomDialog'

    entry = Gtk.Template.Child(name='entry')

    def __init__(self):
        super().__init__()

    def get_entry_text(self):
        return self.entry.get_text()


if __name__ == '__main__':
    pass
