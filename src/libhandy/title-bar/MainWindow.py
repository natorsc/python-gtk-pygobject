# -*- coding: utf-8 -*-
"""Handy.TitleBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version('Handy', '0.0')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.TitleBar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        self.hdy_title_bar = Handy.TitleBar.new()
        self.set_titlebar(titlebar=self.hdy_title_bar)

        hdy_header_bar = Handy.HeaderBar.new()
        hdy_header_bar.set_title(title='Handy.TitleBar')
        hdy_header_bar.set_subtitle(subtitle='Handy.TitleBar')
        hdy_header_bar.set_show_close_button(setting=True)
        self.hdy_title_bar.add(widget=hdy_header_bar)

        btn_selection_mode = Gtk.Button.new_from_icon_name(
            icon_name='object-select-symbolic',
            size=Gtk.IconSize.BUTTON,
        )
        btn_selection_mode.connect(
            'clicked',
            self._enable_and_disable_selection_mode,
        )
        hdy_header_bar.pack_end(child=btn_selection_mode)

        self.show_all()

    def _enable_and_disable_selection_mode(self, widget):
        selection_mode = self.hdy_title_bar.get_selection_mode()
        if selection_mode:
            self.hdy_title_bar.set_selection_mode(selection_mode=False)
        else:
            self.hdy_title_bar.set_selection_mode(selection_mode=True)


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
