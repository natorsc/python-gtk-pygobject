# -*- coding: utf-8 -*-
"""Criando uma janela."""

# Importando a biblioteca gnome introspection.
import gi

# Definindo que o aplicativo deve ser executado no GTK 3.
# Isso porque um computador pode ter mais de uma versão do GTK.
gi.require_version(namespace='Gtk', version='3.0')

# Importando os widgets do GTK.
from gi.repository import Gtk

# Criando a janela principal.
win = Gtk.ApplicationWindow()

# Configurando a janela principal.
win.set_title(title='Python com GTK')
win.set_default_size(width=1366 / 2, height=768 / 2)
win.set_position(position=Gtk.WindowPosition.CENTER)
win.set_default_icon_from_file(filename='../assets/icons/icon.png')

# Conectando a janela principal ao **evento** de fechar o aplicativo.
# Este evento é disparado quando o botão fechar da janela é pressionado.
win.connect('destroy', Gtk.main_quit)

# Exibindo a janela.
win.show_all()

# Iniciando o loop.
Gtk.main()
