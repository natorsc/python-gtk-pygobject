# -*- coding: utf-8 -*-
"""Gtk.SearchBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    _current_button_state = False

    btn_search = Gtk.Template.Child(name='btn_search')
    search_bar = Gtk.Template.Child(name='search_bar')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

    @Gtk.Template.Callback()
    def on_btn_search_clicled(self, widget):
        self._current_button_state = widget.get_active()
        self._show_hidden_search_bar()

    @Gtk.Template.Callback()
    def key_press_event(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)
        if shortcut in ('Ctrl+F', 'Ctrl+Mod2+F'):
            self._show_hidden_search_bar()
            self._change_button_state()
        if shortcut == 'Mod2+Esc' and self.search_bar.get_search_mode():
            self._show_hidden_search_bar()
            self._change_button_state()
        return True


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
