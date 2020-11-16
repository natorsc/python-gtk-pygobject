# -*- coding: utf-8 -*-
"""Gtk.Window()."""

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version(namespace='Gtk', version='3.0')

# Importando os widgets do Gio e GTK.
from gi.repository import Gio, Gtk


class MainWindow(Gtk.Window):
    """Classe herda de ``Gtk.Window``."""

    def __init__(self, **kwargs):
        """Construtor."""
        super().__init__(**kwargs)

        # Configurando a janela principal.
        self.set_title(title='Gtk.Window')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Widgets.
        button = Gtk.Button.new_with_label('Clique Aqui')
        button.connect('clicked', self.on_button_clicked)
        self.add(widget=button)
        self.show_all()

    def on_button_clicked(self, widget):
        window = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
        window.set_modal(modal=True)
        window.set_title(title='Outra janela')
        window.set_default_size(width=1366 / 2, height=768 / 2)
        window.set_size_request(width=1366 / 2, height=768 / 2)
        window.set_position(position=Gtk.WindowPosition.CENTER)
        window.set_default_icon_from_file(filename='../../assets/icons/person.png')
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
