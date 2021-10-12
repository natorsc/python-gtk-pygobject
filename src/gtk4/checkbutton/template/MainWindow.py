# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.CheckButton()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='MainWindow.cmb.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self, **kwargs):
        """Construtor."""
        super().__init__(**kwargs)

        # Configuração dos widgets aqui:
        # ...

    @Gtk.Template.Callback()
    def on_check_button_toggled(self, widget):
        if widget.get_active():
            print('Botão marcado')
        else:
            print('Botão desmarcado')


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
