# -*- coding: utf-8 -*-
"""Python e GTK 4: Criando executáveis com Cx_Freeze."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('ui', 'MainWindow.ui'))


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='ui/MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    entry = Gtk.Template.Child(name='entry')
    label = Gtk.Template.Child(name='label')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configuração dos widgets aqui:
        # ...

    @Gtk.Template.Callback()
    def on_button_clicked(self, widget):
        if self.entry.get_text():
            self.label.set_label(str=self.entry.get_text())
        else:
            self.label.set_label(str='Digite algo no campo acima!')


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
