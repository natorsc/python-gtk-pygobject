# -*- coding: utf-8 -*-
""" Handy.DialerButton.

Botão utilizado para representar numeros e digitos.
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title=' Handy.DialerButton')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        # Criando o DialerButton.
        # O primeiro elemento da string é utilizada no label principal e
        # os demais elementos são utilizado no label secundário.
        hdy_dialer_button = Handy.DialerButton.new('2ABC')
        hdy_dialer_button.connect('clicked', self.on_button_clicked)
        vbox.pack_start(
            child=hdy_dialer_button,
            expand=False,
            fill=False,
            padding=0,
        )

    @staticmethod
    def on_button_clicked(button):
        print(f'Digito do botão pressionado: {button.get_digit()}')
        print(f'Simbolo do botão pressionado: {button.get_symbols()}')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
