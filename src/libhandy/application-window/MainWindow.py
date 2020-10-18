# -*- coding: utf-8 -*-
"""Utilizando uma classe para criar e configurar a janela principal.

Disponível a partir da versão 1.0?
"""

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version('Gtk', '3.0')
# Definindo a versão da biblioteca libhandy.
gi.require_version('Handy', '0.0')

# Importando as bibliotecas Gio e GTK.
from gi.repository import Gtk, Gio
# Importando a biblioteca libhandy.
from gi.repository import Handy


class MainWindow(Handy.ApplicationWindow):
    """Classe herda de ``Handy.ApplicationWindow``."""

    def __init__(self, **kwargs):
        """Construtor."""
        super().__init__(**kwargs)

        # Configurando a janela principal.
        self.set_title(title='Python com GTK e libhandy')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # O seu código aqui:
        # ...

        self.show_all()


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
