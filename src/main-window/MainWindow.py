# -*- coding: utf-8 -*-
"""Utilizando uma classe para criar e configurar a janela principal."""

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version(namespace='Gtk', version='3.0')

# Importando os widgets do GTK.
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    """Classe herda de ``Gtk.ApplicationWindow``."""

    def __init__(self):
        """Construtor."""
        super().__init__()

        # Configurando a janela principal.
        self.set_title(title='Python com GTK')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../assets/icons/icon.png')


if __name__ == '__main__':
    # Criando a janela principal.
    win = MainWindow()

    # Conectando a janela principal ao evento de fechar o aplicativo.
    # Este evento é disparado quando o botão fechar da janela é pressionado.
    win.connect('destroy', Gtk.main_quit)

    # Exibindo a janela.
    win.show_all()

    # Iniciando o loop.
    Gtk.main()
