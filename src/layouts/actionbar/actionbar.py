# -*- coding: utf-8 -*-
"""Contêiner do tipo ActionBar Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Lista com o nome dos ícones.
    icons = ['call-start-symbolic', 'call-stop-symbolic',
             'contact-new-symbolic', 'address-book-new-symbolic']

    def __init__(self):
        super().__init__()

        self.set_title(title='ActionBar Layout')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        actionbar = Gtk.ActionBar.new()
        vbox.pack_end(child=actionbar, expand=False, fill=False, padding=0)

        # Loop de repetição para ler a lista com o nome dos ícones.
        for icon in self.icons:
            # Criando um botão com ícone dentro.
            button = Gtk.Button.new_from_icon_name(
                icon_name=icon,
                size=Gtk.IconSize.BUTTON
            )
            actionbar.pack_start(child=button)

            # Adicionando os botões no final do ActionBar.
            # actionbar.pack_end(child=botao)


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
