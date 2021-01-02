# -*- coding: utf-8 -*-
"""Gtk.Window()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gio


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, widget):
        window = Gtk.Window.new(type=Gtk.WindowType.TOPLEVEL)
        window.set_transient_for(parent=self)
        window.set_modal(modal=True)
        window.set_title(title='Gtk.Window')
        window.set_default_size(width=1366 / 3, height=768 / 3)
        window.set_default_icon_from_file(filename='../../../assets/icons/person.png')
        window.show_all()


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
