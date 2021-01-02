# -*- coding: utf-8 -*-
"""Gtk.Statusbar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    statusbar = Gtk.Template.Child(name='statusbar')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.context_id = self.statusbar.get_context_id(
            context_description='exemplo',
        )

    @Gtk.Template.Callback()
    def statusbar_show_msg(self, widget):
        self.message_id = self.statusbar.push(
            context_id=self.context_id,
            text='Texto que será exibido no statusbar.',
        )

    @Gtk.Template.Callback()
    def statusbar_remove_msg(self, widget):
        # self.statusbar.remove(
        #     context_id=self.context_id,
        #     message_id=self.message_id,
        # )
        self.statusbar.remove_all(context_id=self.context_id)


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
