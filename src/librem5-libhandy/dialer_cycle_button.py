# -*- coding: utf-8 -*-
"""DialerCycleButton.

Este botão é utilizado para represetanar simbolos como #, +, etc.
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        # Configurando a janela principal.
        self.set_title(title='DialerCycleButton')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        self.set_border_width(border_width=10)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(widget=vbox)

        # Criando o DialerButton.
        # O primeiro elemento da string é utilizada no label principal e
        # os demais elementos são utilizado no label secundário.
        hdy_dialer_cycle_button = Handy.DialerCycleButton.new('#123')
        hdy_dialer_cycle_button.connect('clicked', self.on_button_clicked)
        # hdy_dialer_cycle_button.set_cycle_timeout(timeout=5000)
        vbox.pack_start(
            child=hdy_dialer_cycle_button,
            expand=False,
            fill=False,
            padding=0,
        )

    @staticmethod
    def on_button_clicked(button):
        print(button.is_cycling())
        print(button.get_cycle_timeout())
        print(f'Simbolo do botão pressionado: {button.get_current_symbol()}')


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
