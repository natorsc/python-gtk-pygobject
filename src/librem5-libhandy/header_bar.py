# -*- coding: utf-8 -*-
"""Handy.HeaderBar."""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_title(title='Handy.HeaderBar')
        self.set_default_size(width=768 / 2, height=1366 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../../images/icons/icon.png')
        self.set_border_width(border_width=10)

        hdy_header_bar = Handy.HeaderBar.new()
        hdy_header_bar.set_title(title='Título')
        hdy_header_bar.set_subtitle(subtitle='sub-título')
        hdy_header_bar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=hdy_header_bar)

        button_mail = Gtk.Button.new_from_icon_name(
            icon_name='mail-send-receive-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        button_mail.connect('clicked', self._send_mail)
        hdy_header_bar.pack_end(child=button_mail)

        # Criando um Box Layout horizontal para conter os botões com seta.
        # Utilizando um Box Layout os botões ficam melhore distribuidos.
        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        # Adicionando o Box Layout no começo do HeaderBar.
        hdy_header_bar.pack_start(child=hbox)

        button_left_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        button_left_arrow.connect('clicked', self._left_arrow)
        hbox.add(widget=button_left_arrow)

        button_right_arrow = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic-rtl',
            size=Gtk.IconSize.BUTTON
        )
        button_right_arrow.connect('clicked', self._right_arrow)
        hbox.add(widget=button_right_arrow)

        # Adicionando um widget do tipo TextView()
        # na janela principal (só para não ficar vazio).
        self.add(widget=Gtk.TextView.new())

    @staticmethod
    def _send_mail(widget):
        print('Você clicou no botão que tem o icone de enviar/receber email')

    @staticmethod
    def _left_arrow(widget):
        print('Você clicou no botão que tem uma seta para a esquerda')

    @staticmethod
    def _right_arrow(widget):
        print('Você clicou no botão que tem uma seta para a direita')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
