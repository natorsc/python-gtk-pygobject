# -*- coding: utf-8 -*-
"""Python e GTK: Como criar um executável com Cx_Freeze no Windows."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


@Gtk.Template(filename='./ui/MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    entry = Gtk.Template.Child(name='entry')
    label = Gtk.Template.Child(name='label')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def _on_button_clicked(self, button):
        if self.entry.get_text():
            self.label.set_label(str=self.entry.get_text())
        else:
            self.label.set_label(str='Digite algo no campo acima!')


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.CodigoNinja',
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


def run_make_include_files():
    import os
    from windows.make_include_files import make_include_files_by_pid
    pid = os.getpid()
    make_include_files_by_pid(pid=pid, path='windows')


if __name__ == '__main__':
    import sys

    app = Application()

    # Gerando o arquivo include_files.py que será utilizado pelo Cx_Freeze.
    # run_make_include_files()

    app.run(sys.argv)
