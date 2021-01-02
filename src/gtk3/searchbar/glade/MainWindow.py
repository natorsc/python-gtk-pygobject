# -*- coding: utf-8 -*-
"""Gtk.SearchBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:
    _current_button_state = False

    def __init__(self):

        self.btn_search = builder.get_object(name='btn_search')
        self.search_bar = builder.get_object(name='search_bar')

    def _show_hidden_search_bar(self):
        if self.search_bar.get_search_mode():
            self.search_bar.set_search_mode(search_mode=False)
        else:
            self.search_bar.set_search_mode(search_mode=True)

    def _change_button_state(self):
        if self._current_button_state:
            self.btn_search.set_state_flags(flags=Gtk.StateFlags.NORMAL, clear=True)
            self._current_button_state = False
        else:
            self.btn_search.set_state_flags(flags=Gtk.StateFlags.ACTIVE, clear=True)
            self._current_button_state = True

    def on_btn_search_clicled(self, widget):
        self._current_button_state = widget.get_active()
        self._show_hidden_search_bar()

    def key_press_event(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)
        if shortcut in ('Ctrl+F', 'Ctrl+Mod2+F'):
            self._show_hidden_search_bar()
            self._change_button_state()
        if shortcut == 'Mod2+Esc' and self.search_bar.get_search_mode():
            self._show_hidden_search_bar()
            self._change_button_state()
        return True


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
