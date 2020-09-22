# -*- coding: utf-8 -*-
"""Lendo arquivo de interface gerado pelo Gnome Glade."""

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:
    """Classe/Objeto."""

    def __init__(self):
        """Construtor."""

        # Acessar os widgets da interface com builder.get_object(name) aqui:
        # ...


if __name__ == '__main__':
    # Criando uma instancia do Builder.
    builder = Gtk.Builder.new()
    # Acessando/lendo arquivo de interface.
    builder.add_from_file(filename='./MainWindow.glade')
    # Registrando widget, métodos, etc.
    builder.connect_signals(obj_or_map=Handler())

    # Listando todos os widgets disponíveis no arquivo de interface.
    # print(builder.get_objects())

    # Acessando a janela que foi criada no arquivo de interface.
    win = builder.get_object(name='MainWindow')

    # Conectando o evento de fechar ao botão fechar da janela.
    win.connect('destroy', Gtk.main_quit)

    # Exibindo a janela.
    win.show_all()

    # Loop da interface.
    Gtk.main()
