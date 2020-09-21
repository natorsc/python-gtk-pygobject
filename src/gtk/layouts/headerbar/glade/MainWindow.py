# -*- coding: utf-8 -*-
"""Contêiner do tipo Headerbar Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class Handler:

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
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
