# -*- coding: utf-8 -*-
""" Handy.Dialer.

Widget constrói um discador completo.
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


def _on_dialer_button_clicked(dialer, number):
    print(f'Discando para: {number}')
    print(f'Parâmetro dialer: {dialer}')
    print(f'Parâmetro number: {number}')
    print('---\n')


def _on_symbol_clicked(dialer, number):
    print(f'Numeros digitados: {dialer.get_number()}')
    print('Parâmetro dialer:', dialer)
    print('Parâmetro number:', number)
    print('---\n')


def _on_return_clicked(dialer):
    print(f'Numeros digitados: {dialer.get_number()}')
    print('Parâmetro dialer:', dialer)
    print('---\n')


# Criando a janela principal.
win = Gtk.ApplicationWindow()

# Configurando a janela principal.
win.set_title(title='Exemplo de discador com Python (libhandy)')
win.set_default_size(width=768 / 2, height=1366 / 2)
win.set_position(position=Gtk.WindowPosition.CENTER)
win.set_default_icon_from_file(filename='../../../images/icons/icon.png')
win.set_border_width(border_width=10)

# Criando do discador.
dialer = Handy.Dialer.new()
# Callback disparado quando o botão de DISCAR é pressionado.
dialer.connect('submitted', _on_dialer_button_clicked)
# Callback disparado quando as TECLAS do dicador são pressionadas.
dialer.connect('symbol-clicked', _on_symbol_clicked)
# Callback disparado quando o botão de APAGAR é pressionado.
dialer.connect('deleted', _on_return_clicked)
win.add(widget=dialer)

# Conectando a janela principal ao evento de fechar o aplicativo.
# Este evento é disparado quando o botão fechar da janela é pressionado.
win.connect('destroy', Gtk.main_quit)

# Exibindo a janela.
win.show_all()

# Iniciando o loop.
Gtk.main()
