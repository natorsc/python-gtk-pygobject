# -*- coding: utf-8 -*-
""" Handy.Dialer.

Widget constrói um discador completo.
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='libhandy')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../images/icons/icon.png')
        self.set_border_width(border_width=10)

        hdy_dialer = Handy.Dialer.new()
        # Callback disparado quando o botão de DISCAR é pressionado.
        hdy_dialer.connect('submitted', self.on_dialer_button_clicked)
        # Callback disparado quando as TECLAS do dicador são pressionadas.
        hdy_dialer.connect('symbol-clicked', self.on_symbol_clicked)
        # Callback disparado quando o botão de APAGAR é pressionado.
        hdy_dialer.connect('deleted', self.on_return_clicked)
        self.add(widget=hdy_dialer)

    def on_dialer_button_clicked(self, dialer, number):
        print(f'Discando para: {number}')
        print(f'Parâmetro dialer: {dialer}')
        print(f'Parâmetro number: {number}')
        print('---\n')

    def on_symbol_clicked(self, dialer, number):
        print(f'Numeros digitados: {dialer.get_number()}')
        print('Parâmetro dialer:', dialer)
        print('Parâmetro number:', number)
        print('---\n')

    def on_return_clicked(self, dialer):
        print(f'Numeros digitados: {dialer.get_number()}')
        print('Parâmetro dialer:', dialer)
        print('---\n')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
