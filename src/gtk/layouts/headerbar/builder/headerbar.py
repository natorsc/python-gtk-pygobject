# -*- coding: utf-8 -*-
"""Contêiner do tipo Headerbar Layout."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./headerbar.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    @Gtk.Template.Callback()
    def _send_mail(self, button):
        print('Você clicou no botão que tem o icone de enviar/receber email')

    @Gtk.Template.Callback()
    def _left_arrow(self, button):
        print('Você clicou no botão que tem uma seta para a esquerda')

    @Gtk.Template.Callback()
    def _right_arrow(self, button):
        print('Você clicou no botão que tem uma seta para a direita')


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
