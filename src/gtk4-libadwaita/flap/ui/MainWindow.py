# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.ActionBar()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk, Adw


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'DeletarWindow'

    # Acessando o widget (componente) com id="flap".
    flap = Gtk.Template.Child()

    def __init__(self, **kwargs):
        """Construtor."""
        super().__init__(**kwargs)

        # Configuração dos widgets aqui:
        # ...

    @Gtk.Template.Callback()
    def on_flap_button_toggled(self, widget):
        self.flap.set_reveal_flap(not self.flap.get_reveal_flap())


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id='br.natorsc.Deletar',
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
