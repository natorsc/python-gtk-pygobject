# -*- coding: utf-8 -*-
"""Lendo arquivo de interface gerado pelo Builder."""

import sys

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


# @Gtk.Template(string, filename, resource_path)
@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    """Classe herda de ``Gtk.ApplicationWindow``."""
    # Variável deve ter o mesmo nome da propriedade ``class`` do arquivo de inteface.
    # <template class="MainWindow" parent="GtkApplicationWindow">
    __gtype_name__ = 'MainWindow'

    # Acessar os widgets da interface com Gtk.Template.Child(name) aqui:
    # ...

    def __init__(self, **kwargs):
        """Construtor."""
        super().__init__(**kwargs)

        # Configuração dos widgets aqui:
        # ...


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
    app = Application()
    app.run(sys.argv)
